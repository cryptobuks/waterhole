from openerp import api, fields, models


class Farm(models.Model):
    _inherit = 'purchase.order'

    waterhole_id = fields.Many2one('waterhole')
    owner = fields.Char(related='waterhole_id.owner', readonly=True)
    cubic_meters = fields.Float(related='waterhole_id.cubic_meters', readonly=True)
    coordinates = fields.Char(related='waterhole_id.coordinates', readonly=True)
    expiration_date = fields.Date(related="waterhole_id.expiration_date", readonly=True)
