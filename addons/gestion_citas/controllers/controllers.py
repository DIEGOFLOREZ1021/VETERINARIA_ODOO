from odoo import http
from odoo.http import request

class GestionCitasController(http.Controller):

    @http.route('/citas', type='http', auth='public', website=True)
    def citas_list(self, **kwargs):
        citas = request.env['gestion.cita'].sudo().search([])
        return request.render('gestion_citas.web_citas_list', {'citas': citas})

    @http.route('/citas/<int:cita_id>', type='http', auth='public', website=True)
    def cita_detail(self, cita_id, **kwargs):
        cita = request.env['gestion.cita'].sudo().browse(cita_id)
        return request.render('gestion_citas.web_cita_detail', {'cita': cita})