from odoo import models, fields


class Building(models.Model) :
    _name = 'building'
    _description = 'Building'
    # _rec_name = 'code'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    no = fields.Integer()
    code = fields.Char()
    description = fields.Text()
    active = fields.Boolean(default=True)

