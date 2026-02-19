# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class GestionPersonalVeterinaria(http.Controller):

    @http.route('/veterinarios', auth='public', website=True)
    def veterinarios_list(self, **kwargs):
        veterinarios = request.env['gestion_personal_veterinaria.veterinario'].sudo().search([])
        return request.render('gestion_personal_veterinaria.web_veterinarios_list', {
            'veterinarios': veterinarios
        })

    @http.route('/veterinarios/<model("gestion_personal_veterinaria.veterinario"):veterinario>', auth='public', website=True)
    def veterinario_detail(self, veterinario, **kw):
        return request.render('gestion_personal_veterinaria.web_veterinario_detail', {
            'veterinario': veterinario
        })
