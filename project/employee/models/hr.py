from odoo import api, fields, models


class hr(models.Model):
    _name = "employer.hr"
    _description = "Employee_hr_records"
    _inherit = ['mail.thread']

    name = fields.Char(string='name')
    age = fields.Integer(string="age")
    gender = fields.Selection([("male", "Male"), ("female", "Female"), ("others", "Others")],string="gender")
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
