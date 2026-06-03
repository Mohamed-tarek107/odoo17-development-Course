from odoo import models, fields


class Property(models.Model):
    _name = 'owner'
    _description = 'Owner'

    name = fields.Char(required=True, default='New', size=10)
    phone = fields.Char()
    address = fields.Char()
