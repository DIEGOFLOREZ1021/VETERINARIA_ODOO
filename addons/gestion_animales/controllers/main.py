# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class GestionAnimales(http.Controller):
    @http.route('/animales', auth='public', website=True)
    def animales_list(self, **kwarsg):
            animales = request.env['gestion.animal'].sudo().search([])
            return request.render('gestion_animales.web_animales_list',{
                  'animales': animales
            })

    @http.route('/animales/<model("gestion.animal"):animal>', auth='public', website=True)
    def animales_detail(self, animal, **kw):
        return http.request.render('gestion_animales.web_animal_detail',{
             'animal': animal
        })

#     @http.route('/gestion_animales/gestion_animales/objects/<model("gestion_animales.gestion_animales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_animales.object', {
#             'object': obj
#         })

