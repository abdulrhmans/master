# -*- coding: utf-8 -*-

from odoo import models, fields


class RestaurantPrinter(models.Model):
    _inherit = 'restaurant.printer'

    printer_port = fields.Integer(string="Port", required=True, default=9100)
