# -*- coding: utf-8 -*-
from odoo import models, fields


class GestionVeterinario(models.Model):
    _name = "gestion_personal_veterinaria.veterinario"
    _description = "Veterinarios"

    name = fields.Char(string="Nombre", required=True)
    specialty = fields.Char(string="Especialidad")
    phone = fields.Char(string="Telefono")
    email = fields.Char(string="Email")
    active = fields.Boolean(string="Activo", default=True)
