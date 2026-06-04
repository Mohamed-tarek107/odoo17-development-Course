from odoo import models, fields


class Owner(models.Model):
    _name = 'owner'
    _description = 'Owner'

    name = fields.Char(required=True, default='New', size=10)
    phone = fields.Char()
    address = fields.Char()
    #many2one howa ely bysm3 fyl database bs
    property_ids = fields.One2many('property','owner_id')