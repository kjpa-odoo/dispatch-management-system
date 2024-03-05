from odoo import models, fields

class DockModel(models.Model):
    _name='dock.model'

    name=fields.Char(string='Dock')