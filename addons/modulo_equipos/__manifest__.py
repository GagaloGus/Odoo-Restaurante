# -*- coding: utf-8 -*-
{
    'name': "modulo_equipos",

    'summary': "Modulo obligatorio: miembros del grupo",

    'description': """
Long description of module's purpose
    """,

    'author': "Paula",
    #'website': "https://www.yourcompany.com",

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
        'views/modulo_equipo_menu.xml',
        'views/modulo_equipo_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    #
    'application': True,
    'installable': True
}

