# -*- coding: utf-8 -*-
{
    'name': "POS NETWORK PRINTER",
    'summary': """
        Manage Network ESC/POS Printer in Point of sale without POS Box""",
    'description': """
        Manage Network ESC/POS Printer in Point of sale without POS Box
    """,
    'author': "Aimé Jules Andrinirina",
    'website': "",
    'license': 'LGPL-3',
    'category': 'Point Of Sale',
    'version': '11.0.1.1',
    'images': ['images/cover.jpg'],
    'depends': ['base', 'point_of_sale'],
    'qweb': ['static/src/xml/pos.xml'],
    'data': [
        # security
        'security/ir.model.access.csv',
        # views
        'views/assets.xml',
        'views/pos_config_view.xml',
        'views/network_printer_view.xml',
    ],
    'price': '350',
    'currency': 'EUR',

}
