from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'

    name = fields.Char(required=1, default='New', size=10)
    description = fields.Text()
    postcode = fields.Char(required=1)
    Date_availability = fields.Date()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_rooms = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
    ('north', 'North'),
    ('south', 'South'),
    ('east', 'East'),
    ('west', 'West'),
])

    @api.constraints('bedrooms')
    def _check_bedroom_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                # print("not valid")
                raise ValidationError('Add valid number of bedrooms')