# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RestaurantPrinterInherit(models.Model):
    _inherit = 'restaurant.printer'

    connector_id = fields.Many2one('printer.connector', string='Connector', required=True)