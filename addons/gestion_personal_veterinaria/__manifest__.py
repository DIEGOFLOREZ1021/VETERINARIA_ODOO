# -*- coding: utf-8 -*-
{
    "name": "Gestion Personal Veterinaria",
    "summary": "Modulo para gestionar veterinarios",
    "description": """
Proyecto de clínica veterinaria:
- Backend: gestion de veterinarios
- Website: listado y detalle publico
""",
    "author": "Grupo Veterinaria",
    "website": "",
    "category": "Services",
    "version": "1.0",

    "depends": ["base", "website"],

    "data": [
        "security/ir.model.access.csv",
        "views/veterinario_views.xml",
        "views/templates.xml",
        "views/veterinario_menu.xml",
    ],

    "application": True,
    "installable": True,
}
