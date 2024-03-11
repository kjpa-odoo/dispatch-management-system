from odoo import models, fields, api


class BatchTransfer(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("dock.model", stirng="Dock")
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one(
        "fleet.vehicle.model.category",
        string="Vehicle Category",
        placeholder="e.g. Semi-Truck",
    )
    tot_weight = fields.Float(
        string="Weight", compute="_compute_total_weight", store=True
    )
    tot_volume = fields.Float(
        string="Volume", compute="_compute_total_volume", store=True
    )
    weight_progressbar = fields.Float(
        string="Weight", compute="_compute_weight_ref", store=True
    )
    volume_progressbar = fields.Float(
        string="volume", compute="_compute_volume_ref", store=True
    )
    transfer_count = fields.Integer(
        string="Transfers", compute="_compute_tranfer_count", store=True
    )

    @api.depends("tot_weight", "vehicle_category_id")
    def _compute_weight_ref(self):
        for record in self:
            if record.vehicle_category_id:
                record.weight_progressbar = (
                    record.tot_weight / record.vehicle_category_id.max_weight
                ) * 100

    @api.depends("tot_volume", "vehicle_category_id")
    def _compute_volume_ref(self):
        for record in self:
            if record.vehicle_category_id:
                record.volume_progressbar = (
                    record.tot_volume / record.vehicle_category_id.max_volume
                ) * 100

    @api.depends("vehicle_category_id", "picking_ids.weight")
    def _compute_total_weight(self):
        print("i'm changed")
        for record in self:
            tot = 0
            for p in record.picking_ids:
                tot += p.weight
            record.tot_weight = tot

    @api.depends("vehicle_category_id", "picking_ids.weight")
    def _compute_total_volume(self):
        for record in self:
            tot = 0
            for p in record.picking_ids:
                tot += p.volume
            record.tot_volume = tot

    @api.depends("picking_ids")
    def _compute_tranfer_count(self):
        for record in self:
            record.transfer_count = len(record.picking_ids)

    @api.depends("tot_weight", "tot_volume")
    def _compute_display_name(self):
        for record in self:
            record.display_name = (
                record.name
                + " ("
                + str(record.tot_weight)
                + "kg, "
                + str(record.tot_volume)
                + "m\u00b3)"
            )
