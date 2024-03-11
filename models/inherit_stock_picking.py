from odoo import models,fields,api

class StockPicking(models.Model):
    _inherit='stock.picking'

    weight=fields.Float(string="Weight", compute='_compute_weight')
    volume=fields.Float(string="volume", compute='_compute_volume')

    @api.depends('product_id', 'product_id.weight', 'move_ids.quantity')
    def _compute_weight(self):
        for record in self:
            dummy = 0
            for m in record.move_line_ids:
                dummy += m.product_id.weight * m.quantity
            record.weight = dummy
    
    @api.depends('product_id', 'product_id.volume','move_ids.quantity')
    def _compute_volume(self):
        for record in self:
            dummy = 0
            for m in record.move_line_ids:
                dummy += m.product_id.volume * m.quantity
            record.volume = dummy