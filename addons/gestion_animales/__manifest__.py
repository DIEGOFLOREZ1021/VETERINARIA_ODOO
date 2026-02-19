# -*- coding: utf-8 -*-
{
    'name': "gestion animales",

    'summary': "Gestion interna de los animales",

    'description': """
En este modulo se realiza toda la gestion de los animales, sus datos, su historial medico, sus vacunas, etc
    """,

    'author': "Veterinaria Odoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'App Gestion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/gestion_animal_view.xml',
        'views/gestion_animal_search.xml',
        'views/gestion_animal_menu.xml',
        'views/templates.xml',
    ],
    
    "application": True,
    "installable": True,
}

