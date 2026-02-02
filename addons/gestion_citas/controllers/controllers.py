# -*- coding: utf-8 -*-
# from odoo import http


# class GestionCitas(http.Controller):
#     @http.route('/gestion_citas/gestion_citas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_citas/gestion_citas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_citas.listing', {
#             'root': '/gestion_citas/gestion_citas',
#             'objects': http.request.env['gestion_citas.gestion_citas'].search([]),
#         })

#     @http.route('/gestion_citas/gestion_citas/objects/<model("gestion_citas.gestion_citas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_citas.object', {
#             'object': obj
#         })

