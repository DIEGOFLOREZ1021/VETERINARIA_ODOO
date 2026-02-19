from odoo import models, fields


class GestionAnimal(models.Model):
    _name = 'gestion.animal'
    _description = 'Animales Veterinaria Odoo'

    # Identificación
    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string='Código / Chip',required=True)
    active = fields.Boolean(String='Activo / Inactivo', default=True)

    # Clasificación
    species = fields.Char(string='Especie', required=True)
    breed = fields.Char(string='Raza', )
    sex = fields.Selection([('male', 'Macho'),('female', 'Hembra')],string='Sexo')
    color = fields.Char(string='Color')

    # Datos biológicos
    birth_date = fields.Date(string='Fecha de nacimiento')
    age = fields.Integer(string='Edad (años)', required=True)
    weight = fields.Float(string='Peso (kg)')
    height = fields.Float(string='Altura (cm)')

    # Propiedad / responsables
    owner = fields.Char(string='Nombre dueño', required=True)
    veterinarian_id = fields.Char(string='Veterinario', required=True)

    # Salud
    health_state = fields.Selection(
        [
            ('healthy', 'Sano'),
            ('sick', 'Enfermo'),
            ('treatment', 'En tratamiento'),
            ('critical', 'Crítico')
        ],
        string='Estado de salud',
        default='healthy'
    )
    sterilized = fields.Boolean(string='Esterilizado')
    last_vaccine_date = fields.Date(string='Última vacunación')
    notes_medical = fields.Text(string='Notas médicas')

