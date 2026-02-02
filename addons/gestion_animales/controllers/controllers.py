# -*- coding: utf-8 -*-
# from odoo import http


# class GestionAnimales(http.Controller):
#     @http.route('/gestion_animales/gestion_animales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_animales/gestion_animales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_animales.listing', {
#             'root': '/gestion_animales/gestion_animales',
#             'objects': http.request.env['gestion_animales.gestion_animales'].search([]),
#         })

#     @http.route('/gestion_animales/gestion_animales/objects/<model("gestion_animales.gestion_animales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_animales.object', {
#             'object': obj
#         })

