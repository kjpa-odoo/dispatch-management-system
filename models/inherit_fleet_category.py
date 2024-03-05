from odoo import models,fields,api

class FleetCategory(models.Model):
    _inherit='fleet.vehicle.model.category'

    max_weight=fields.Float(string='Max weight(kg)')
    max_volume=fields.Float(string='Max Volume(m\u00b3)')
    
    def _compute_display_name(self):
        for record in self:
            res = "%s (%skg, %sm\u00b3)" % (record.name, record.max_weight, record.max_volume)
            record.display_name=res