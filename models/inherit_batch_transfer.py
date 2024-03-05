from odoo import models,fields,api

class BatchTransfer(models.Model):
    _inherit='stock.picking.batch'

    dock_id = fields.Many2one('dock', stirng='Dock')
    vehicle_id=fields.Many2one('fleet.vehicle', string='Vehicle')
    vehicle_category_id=fields.Many2one('fleet.vehicle.model.category',string='Vehicle Category',placeholder='e.g. Semi-Truck')
    tot_weight=fields.Float(string='Weight', compute='_compute_total_weight', store=True)
    tot_volume=fields.Float(string='Volume', compute='_compute_total_volume', store=True)
    weight_progressbar=fields.Float(string="Weight", compute='_compute_weight_ref')
    volume_progressbar=fields.Float(string="volume", compute='_compute_volume_ref')

    @api.depends("vehicle_category_id")
    def dothis(self):
        print("i'm changed")

    @api.depends("tot_weight")
    def _compute_weight_ref(self):
        for record in self:
            record.weight_progressbar = (record.vehicle_category_id.max_weight/record.tot_weight) * 100
    
    @api.depends("vehicle_category_id")
    def _compute_volume_ref(self):
        for record in self:
            record.volume_progressbar = (record.vehicle_category_id.max_volume/record.tot_volume) * 100

    @api.depends('vehicle_category_id')
    def _compute_total_weight(self):
        for record in self:
            tot = 0
            for p in record.picking_ids:
                tot += p.weight
            record.tot_weight=tot

    @api.depends('vehicle_category_id')
    def _compute_total_volume(self):
        for record in self:
            tot = 0
            for p in record.picking_ids:
                tot += p.volume
            record.tot_volume=tot