# -*- coding: utf-8 -*-
{
    'name': "gestion_citas",
    'summary': "Aplicacion para gestionar citas veterinarias",
    'description': """
Esta aplicacion puedes gestionar a que hora, con quien y un poco de informacion del animal para hacer una cita con el cliente o el cliente contigo
    """,
    'author': "Aitor",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/gestion_cita_views.xml',
        'views/gestion_cita_search.xml',
        'views/gestion_cita_menu.xml',
        'views/template.xml',
    ],
    'installable': True,
    'application': True,
    # only loaded in demonstration mode

}

