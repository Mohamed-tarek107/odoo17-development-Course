from odoo import models, fields

class Property(models.Model):
    _name = 'property'

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    Date_availability = fields.Date()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_rooms = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        {'north', 'North'},
        {'south', 'South'},
        {'east', 'East'},
        {'west', 'West'}
    ])


