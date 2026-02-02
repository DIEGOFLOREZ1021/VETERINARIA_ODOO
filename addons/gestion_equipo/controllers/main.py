from odoo import http
from odoo.http import request

class GestionEquipo(http.Controller):
    @http.route('/gestion_equipo', auth='public', website=True)
    def index(self, **kwargs):
        equipos = request.env['gestion.persona'].sudo().search([])
        return request.render('gestion_equipo.web_equipo_list', {
            'equipos': equipos
        })
    @http.route('/equipo/<model("gestion.persona"):persona>', auth='public', website=True)
    def equipo_detail(self, persona, **kw):
        return http.request.render('gestion_equipo.web_equipo_detail', {
            'persona': persona
        })