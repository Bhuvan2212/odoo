from odoo import api, fields, models, _


class employee(models.Model):
    _name = "employer.employee"
    _description = "Employee records"
    _inherit = ['mail.thread']

    name = fields.Char(string="Name", tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female"), ("others", "Others")], string="Gender",
                              tracking=True)
    fresher = fields.Boolean(string="fresher", tracking=True, compute="_compute_cap_name", store=True)
    year_of_experience = fields.Integer(string="year of experience", tracking=True, )
    notes = fields.Text(String="Notes")
    cap_name = fields.Char(string="cap_name", compute="_compute_cap_name")
    ref = fields.Char(string="Reference", default=lambda self: _('New'))
    hr_name = fields.Many2one('employer.hr', required=True, string="HRBP", tracking=True)
    active = fields.Boolean(default=True)
    # status = fields.Selection(selection=[("male", "Male"), ("female", "Female"), ("others", "Others")],  index=True,
    #                           default='male',store=True)
    state = fields.Selection(
        selection=[('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done'), ('cancel', 'Cancelled'), ],
        string='Status',
        required=True,
        tracking=True,
        default='draft',
        store=True)

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"

    @api.depends("name")
    def _compute_cap_name(self):
        for record in self:
            if record.name:
                record.cap_name = record.name.upper()
            else:
                record.cap_name = ""
            if record.year_of_experience < 1:
                record.fresher = True
            else:
                record.fresher = False

    @api.onchange("year_of_experience")
    def _onchange_year_of_experience(self):
        if self.year_of_experience < 1:
            self.fresher = True
        else:
            self.fresher = False

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('employer.employee')
        return super(employee, self).create(vals_list)
