# -*- coding: utf-8 -*-

from xml.etree import ElementTree as ET
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ReceiptTemplate(models.Model):
    _name = 'receipt.template'

    name = fields.Char(string='Template', required=True)
    type = fields.Selection([('ticket', 'Ticket receipt'), ('order', 'Order receipt'), ('bill', 'Bill receipt')], string='Type',
                            required=True, default='ticket')
    template = fields.Text(string='Template', required=True)

    def check_xml_format(self, xml_file):
        try:
            ET.fromstring(xml_file)
            return True
        except:
            return False

    @api.model
    def create(self, values):
        if values.get('template'):
            if self.check_xml_format(values.get('template')) is False:
                raise ValidationError(_('Error in xml format'))
        return super(ReceiptTemplate, self).create(values)

    @api.multi
    def write(self, values):
        if values.get('template'):
            if self.check_xml_format(values.get('template')) is False:
                raise ValidationError(_('Error in xml format'))
        return super(ReceiptTemplate, self).write(values)
