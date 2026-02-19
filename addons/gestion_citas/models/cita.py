from odoo import models, fields
class GestionCita(models.Model):
   _name = "gestion.cita"
   _description = "Gestionar Citas" 

   cname = fields.Char (string = "Nombre del Cliente", required=True)
   cid = fields.Char (string = "Identificacion del Cliente", required=True)
   cphonenum = fields.Char(string ="Telefono del Cliente", required=True)
   cemail = fields.Char(string ="Correo del Cliente")
   caddress = fields.Char(string ="Direccion del Cliente", required=True)
  
   aname = fields.Char(string ="Nombre del Animal", required=True)
   aweight= fields.Float(string ="Peso del Animal", required=True)
   abirthdate = fields.Char(string ="Fecha de Nacimiento del Animal", required=True)
   aid = fields.Char(string = "Identificacion del Animal", required=True)
   
   vname = fields.Char (string = "Nombre del Veterinario asignado", required=True)
   
   timedate= fields.Datetime(string ="Fecha y Hora", required=True)
   motive = fields.Char(string ="Motivo de la cita", required=True)
   state = fields.Char(string ="Estado de la cita", required=True)
   wascalled = fields.Boolean(string="El cliente ha pedido la cita?")
