# -*- coding: utf-8 -*-

from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    use_custom_receipt = fields.Boolean(string='Use custom receipt', default=False)
    ticket_receipt_id = fields.Many2one('receipt.template', string='Ticket receipt', domain=[('type', '=', 'ticket')])
    ticket_order_id = fields.Many2one('receipt.template', string='Order receipt', domain=[('type', '=', 'order')])
    ticket_bill_id = fields.Many2one('receipt.template', string='Bill receipt', domain=[('type', '=', 'bill')])
