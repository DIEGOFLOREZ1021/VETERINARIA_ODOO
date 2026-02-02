# -*- coding: utf-8 -*-
# from odoo import http


# class GestionEquipo(http.Controller):
#     @http.route('/gestion_equipo/gestion_equipo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_equipo/gestion_equipo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_equipo.listing', {
#             'root': '/gestion_equipo/gestion_equipo',
#             'objects': http.request.env['gestion_equipo.gestion_equipo'].search([]),
#         })

#     @http.route('/gestion_equipo/gestion_equipo/objects/<model("gestion_equipo.gestion_equipo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_equipo.object', {
#             'object': obj
#         })

