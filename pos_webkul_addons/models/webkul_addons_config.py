# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE file for full copyright and licensing details.
#   License URL : <https://store.webkul.com/license.html/>
# 
#################################################################################

from odoo import api, fields, models, _

class WebkulPosAddons(models.TransientModel):
    _name = 'webkul.pos.addons'
    _inherit = 'res.config.settings'

    # Product Management
    module_pos_product_pack = fields.Boolean(string="POS Product Pack")
    module_pos_category_filter = fields.Boolean(string="POS Category Filter")
    module_pos_cat_merge = fields.Boolean(string ="POS Merge Category")
    module_pos_shops = fields.Boolean(string="POS Multi Shops")

    # Value Added
    module_pos_carry_bag = fields.Boolean(string="POS Carry Bag")

    #Delivery Method
    module_pos_to_sale_order = fields.Boolean(string="POS Home Delivery")

    # Billing & Invoicing
    module_pos_invoice = fields.Boolean(string="POS  Invoice Automate")
    module_pos_auto_invoice_reconcile = fields.Boolean(string="POS Auto Invoice Reconcile")
    module_pos_invoice_details = fields.Boolean(string="POS Invoice Details")

    # Stock Management
    module_pos_stocks = fields.Boolean(string="POS Stock")
    module_pos_warehouse_management = fields.Boolean(string="POS Warehouse Management")

   
    # POS Orders Management
    module_pos_orders = fields.Boolean(string="POS All Orders List")
    module_pos_order_return = fields.Boolean(strin="POS Order Return")
    module_pos_order_reprint = fields.Boolean(string="POS Order Reprint")
    module_pos_reorder = fields.Boolean(string="POS Order History & Re-Orde")
    module_pos_rounding = fields.Boolean(string="POS Rounding Off Amount")
    
    
    # Prices & Promotion
    module_pos_order_discount = fields.Boolean(string="POS Order Discount")
    module_pos_custom_discount = fields.Boolean(string="POS Custom Discount")
    module_pos_multi_pricelist = fields.Boolean(string="POS Multi Pricelist")
    module_pos_customer_pricelist = fields.Boolean(string="POS Customer Pricelist")
    module_pos_discounted_product = fields.Boolean(string="POS Show Discounted Price")

    # Advertising & Marketing
    module_pos_coupons = fields.Boolean(string="POS Coupons And Vouchers")
    module_pos_loyalty_management = fields.Boolean(string="POS Loyalty & Rewards Program")
    module_pos_membership_cards = fields.Boolean(string="POS Membership Cards")
    module_pos_wallet_management = fields.Boolean(string="POS Wallet Management")

    # Others Useful Module
    module_pos_order_sync = fields.Boolean(string="POS Order Sync")
    module_pos_quotation = fields.Boolean(string="POS Save Quotation")
    module_pos_line_tax = fields.Boolean(string="POS Tax Details")
    module_pos_product_detail = fields.Boolean(string="POS Product Detail")
    moduel_pos_extra_utilities = fields.Boolean(string="POS Extra Utilities")
    module_pos_screen_lock = fields.Boolean(string="POS Screen Lock")
    module_pos_change_logo = fields.Boolean(string="POS Change Logo")
    module_pos_items_count = fields.Boolean(string="POS Items Count")
    module_pos_order_notes = fields.Boolean(string="POS Order Notes")
    module_pos_cash_alert = fields.Boolean(string="POS Cash Drawer Alert")
    module_pos_manage_order_selector = fields.Boolean(string="POS Manage Order Selector")
    module_pos_customer_contacts = fields.Boolean(string="POS Customer Contacts")
    module_pos_merge_lines = fields.Boolean(string="POS Merge Same Products On Adding")
    module_pos_signature = fields.Boolean(string="POS Signature")
    module_pos_custom_messages = fields.Boolean(string="POS Custom Messages")
    module_pos_multiple_receipts = fields.Boolean(string="POS Multiple Receipts")