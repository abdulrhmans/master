# -*- coding: utf-8 -*-

from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    bill_print_mode = fields.Selection([('web', 'Web'), ('network', 'Network')], string='Bill print mode', default='web', required=True)
