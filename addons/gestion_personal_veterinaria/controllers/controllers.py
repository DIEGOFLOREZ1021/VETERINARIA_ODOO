# -*- coding: utf-8 -*-
# from odoo import http


# class GestionPersonalVeterinaria(http.Controller):
#     @http.route('/gestion_personal_veterinaria/gestion_personal_veterinaria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_personal_veterinaria/gestion_personal_veterinaria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_personal_veterinaria.listing', {
#             'root': '/gestion_personal_veterinaria/gestion_personal_veterinaria',
#             'objects': http.request.env['gestion_personal_veterinaria.gestion_personal_veterinaria'].search([]),
#         })

#     @http.route('/gestion_personal_veterinaria/gestion_personal_veterinaria/objects/<model("gestion_personal_veterinaria.gestion_personal_veterinaria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_personal_veterinaria.object', {
#             'object': obj
#         })

