# -*- coding: utf-8 -*-
{
    'name': "POS RESTAURANT NETWORK PRINTER",
    'summary': """
        Manage Network ESC/POS Printer in Point of sale for Restaurant without POS Box - This module depends on pos_network_printer""",
    'description': """
        Manage Network ESC/POS Printer in Point of sale for Restaurant without POS Box - This module depends on pos_network_printer
    """,
    'author': "Aimé Jules Andrinirina",
    'website': "",
    'license': 'LGPL-3',
    'category': 'Point Of Sale',
    'version': '11.0.1.0',
    'images': ['images/cover.jpg'],
    'depends': ['base',
                'pos_network_printer',
                'pos_restaurant',
                ],
    'data': [
        # views
        'views/assets.xml',
        'views/pos_config_view.xml',
        'views/restaurant_printer_view.xml',
    ],
    'price': '30',
    'currency': 'EUR'
}
