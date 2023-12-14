from odoo import api, fields, models

class employee_wizards(models.Model):
    _name = "employee.wizards"
    _description = "Employee wizards records"


    name = fields.Char(string="Name", tracking=True)
