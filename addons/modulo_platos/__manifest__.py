# -*- coding: utf-8 -*-
{
    'name': "modulo_platos",

    'summary': "Modulo encargado de la gestion de platos",

    'description': """
Platooooooooooooooooooooooooooooooooooooooooooooooo
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/platos_menus.xml',
        'views/platos_views.xml',
        'views/platos_web_detalles.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,
    "installable": True,
}

