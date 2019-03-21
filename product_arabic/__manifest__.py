# -*- coding: utf-8 -*-

{
    'name': 'Arabic product name in POS Receipt',
    'version': '11.0.1.0.0',
    'summary': """Generates Arabic product names in POS receipts""",
    'description': """This module enables user to print the product names in Arabic language in POS receipts""",
    'author': "Cybrosys Techno Solutions",
    'company': 'Cybrosys Techno Solutions',
    'website': 'http://www.cybrosys.com',
    'maintainer': 'Cybrosys Techno Solutions',
    'category': 'Point of Sale',
    'depends': ['point_of_sale', 'product'],
    'data': [
        'views/product_arabic.xml',
        'views/reciept_template.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'demo': [],
    'images': ['static/description/banner.jpg'],
    'license': 'OPL-1',
    'price': 9.99,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
}
