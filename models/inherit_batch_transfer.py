from odoo import models,fields,api

class BatchTransfer(models.Model):
    _inherit='stock.picking.batch'

    dock_id = fields.Many2one('dock', stirng='Dock')
    vehicle_id=fields.Many2one('fleet.vehicle', string='Vehicle')
    vehicle_category_id=fields.Many2one('fleet.vehicle.model.category',string='Vehicle Category',placeholder='e.g. Semi-Truck')
    weight=fields.Integer(related='vehicle_category_id.max_weight')
    volume=fields.Integer(related='vehicle_category_id.max_volume')
    weight_ref=fields.Float(compute='_compute_weight')
    volume_ref=fields.Float(compute='_compute_volume')

    @api.depends('vehicle_category_id')
    def _compute_weight(self):
        for record in self:
            tot = 0
            for p in record.picking_ids:
                tot += p.weight
            record.weight_ref = tot
    
    @api.depends('vehicle_category_id')
    def _compute_volume(self):
        for record in self:
            tot = 0
            for p in record.picking_ids:
                tot += p.volume
            volume_ref = tot