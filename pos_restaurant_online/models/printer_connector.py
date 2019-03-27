# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PrinterConnectorInherit(models.Model):
    _inherit = 'printer.connector'

    kitchen_printer_ids = fields.One2many('restaurant.printer', 'connector_id', string='Orders Printers')