# -*- coding: utf-8 -*-
{
    'name': "POS Hide Products Prices in Receipt",
    'summary': "Allows hiding products prices in Point of Sale receipts",
    'description': """
        This module adds a new button in  POS receipt screen that allows hiding products prices in receipt.
    """,
    'author': "Abdullah Ismail",
    'category': 'Point of Sale',
    'version': '0.1',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/pos_config.xml',
        'views/res_config_settings.xml',
    ],
    "assets": {
        'point_of_sale._assets_pos': [
            'pos_hide_receipt_price/static/src/**/*',
        ],
    },
}
