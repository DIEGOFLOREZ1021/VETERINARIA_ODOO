from odoo import models, fields

class GestionPersona(models.Model):
    _name = 'gestion.persona'  
    _description = 'Persona del Equipo'

    img = fields.Image(string='Imagen')
    name = fields.Char(string='Nombre', required=True)
    lastname = fields.Char(string='Apellido', required=True)
    age = fields.Integer(string='Edad')
    grade = fields.Char(string='Grado o Especialidad')
    active = fields.Boolean(string='Activo')
    description = fields.Text(string='Descripción personal')