from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model) :
    _name = 'property'
    _description = 'Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=1, tracking=1)
    description = fields.Text()
    postcode = fields.Char(required=1, tracking=1)
    date_availavlity = fields.Date(tracking=1)
    expected_selling_date = fields.Date(tracking=1)
    is_late = fields.Boolean()
    expected_price = fields.Float(tracking=1)
    selling_price = fields.Float(tracking=1)
    diff = fields.Float(compute="_compute_diff", sotre=True)
    bedrooms = fields.Integer(required=1)
    leaving_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    state = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('sold','Sold'),
        ('closed','Closed'),
    ], default='draft')
    garden_oriantation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ])
    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')
    line_ids = fields.One2many('property.line', 'property_id')


    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This name is exits')
    ]

    @api.depends('expected_price', 'selling_price')
    def _compute_diff(self):
        for rec in self:
            rec.diff = rec.expected_price - rec.selling_price

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self :
            if rec.bedrooms == 0:
                raise ValidationError("Please add valid value of Bedrooms")


    def action_draft(self):
        for rec in self:
            rec.state = "draft"


    def action_pending(self):
        for rec in self:
            rec.write({
                'state': 'pending',
            })

    def action_sold(self):
        for rec in self:
            rec.state= "sold"

    def action_closed(self):
        for rec in self:
            rec.state= "closed"

    def check_expected_selling_date(self):
        print('check_expected_selling_date')
        property_ids = self.search([])
        for rec in property_ids:
            if rec.expected_selling_date and rec.expected_selling_date < fields.date.today():
                rec.is_late = True


class PropertyLine(models.Model) :
    _name = 'property.line'

    property_id = fields.Many2one('property')
    area = fields.Float()
    description = fields.Text()



