# -*- coding: utf-8 -*-
{
    'name': "gestion del equipo",

    'summary': "Gestion interna del equipo de trabajo",

    'description': """
        En este modulo se podra gestionar la informacion del equipo de trabajo, como su nombre, apellido, edad, grado o especialidad y una descripcion personal.
    """,

    'author': "Jorge Jose Cristancho Avila",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/gestion_persona_view.xml',
        'views/gestion_persona_search.xml',
        'views/gestion_persona_menu.xml',
        'views/template.xml',

    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
}

