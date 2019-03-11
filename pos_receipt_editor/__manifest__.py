# -*- coding: utf-8 -*-
{
    'name': "POS RECEIPT EDITOR",
    'summary': """
        Edit Point Of Sale receipt from Odoo backend interface
        """,
    'description': """
        Edit Point Of Sale receipt from Odoo backend interface
    """,
    'author': "Aimé Jules Andrinirina",
    'website': "",
    'license': 'LGPL-3',
    'category': 'Point Of Sale',
    'version': '11.0.1',
    'depends': [
        'base',
        'point_of_sale',
    ],
    'data': [
        # security
        'security/ir.model.access.csv',
        # data
        'data/receipt_template_data.xml',
        # views
        'views/assets.xml',
        'views/receipt_template_view.xml',
        'views/pos_config_view.xml',

    ],
    'price': '45',
    'currency': 'EUR'
}
