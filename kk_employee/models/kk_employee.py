from odoo import fields, models


class KkEmployee(models.Model):
    _name = 'kk.employee'
    _description = 'Employee'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
