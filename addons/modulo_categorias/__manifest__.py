# -*- coding: utf-8 -*-
{
    'name': "Categorias Restaurante",

    'summary': "Modulo de categorias del restaurante",

    'author': "Soledad Moral",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/modulo_categorias_views.xml',
        'views/modulo_categorias_menu.xml',
        #'views/templates.xml',
    ],
    'application': True,
    'installable': True
}

