from openerp import api, fields, models


class Waterhole(models.Model):
    _name = 'waterhole'

    name = fields.Char(string="Watterhole ID", required=True)
    Owner = fields.Many2one('res.partner', required=True)
    Cubic meters = fields.Float(required=True)
    Expiration date = fields.Date(required=True)
    Coordinates = fields.Char(required=True)
