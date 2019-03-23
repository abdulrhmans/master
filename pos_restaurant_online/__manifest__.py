# -*- coding: utf-8 -*-
{
    'name': "POS RESTAURANT ONLINE",
    'summary': """
        Connect local printer to Pos restaurant for online server using Odoo Printer Connector
    """,
    'description': """
        Connect local printer to Pos restaurant for online server using Odoo Printer Connector
    """,
    'author': "Aimé Jules Andrinirina",
    'category': 'Point Of Sale',
    'version': '0.1',
    'depends': [
        'base',
        #'pos_restaurant_network_printer',
        'pos_network_printer_online',
    ],
    'data': [
        # views
        'views/printer_connector_view.xml',
        'views/restaurant_printer_view.xml',
        'views/assets.xml',
    ],
    'license': 'LGPL-3',
    'price': '15',
    'currency': 'EUR',
}
