from odoo import http
from odoo.http import request

class GestionEquipo(http.Controller):
    @http.route('/equipo', auth='public', website=True)
    def index(self, **kwargs):
        equipo = request.env['gestion.persona'].sudo().search([])
        return request.render('gestion_equipo.web_equipo_list', {
            'equipo': equipo
        })
    @http.route('/equipo/<model("gestion.persona"):persona>', auth='public', website=True)
    def equipo_detail(self, persona, **kw):
        return http.request.render('gestion_equipo.web_persona_detail', {
            'persona': persona
        })