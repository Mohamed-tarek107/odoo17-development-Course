from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'
    _description = 'Property'

    name = fields.Char(required=True, default='New', size=10)
    description = fields.Text()
    postcode = fields.Char(required=True)
    Date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    diff = fields.Float(compute='_compute_diff')
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
    # relations if many2one make it singular if many2many or one2many make it plural (best practice)
    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')

    state = fields.Selection([
        ('draft','Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold')
    ], default='draft')


    _sql_constraints = {
        ('unique_name', 'unique("name")', 'this name exist already!')
    }


    def _compute_diff(self):
        for rec in self:
            rec.diff = rec.expected_price - rec.selling_price

    @api.constrains('bedrooms')
    def _check_bedroom_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                # print("not valid")
                raise ValidationError('Add valid number of bedrooms')


    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
            # rec.write({
            #     'state': 'draft'
            # })

    def action_pending(self):
        for rec in self:
            rec.state = 'pending'

    def action_sold(self):
        for rec in self:
            rec.write({
                'state': 'sold'
            })


    # # CRUD Operations -> overriding it from Model:
    # @api.model_create_multi
    # def create(self, vale):
    #     res = super(Property, self).create(vale)
    #     return res
    #
    #
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
    #     res = super()._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
    #     return res
    #
    # def write(self,vale):
    #     res = super(Property, self).write(vale)
    #     return res
    # def unlink(self):
    #     res = super(Property, self).unlink()
    #     return res