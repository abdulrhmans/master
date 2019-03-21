# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductToArabic(models.Model):
    _inherit = 'product.template'

    product_arabic = fields.Char()
