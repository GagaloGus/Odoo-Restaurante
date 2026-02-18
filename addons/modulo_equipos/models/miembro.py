from odoo import models. fields

class EquipoMiembro(models.Model):
    _name = "equipo.miembro"
    _description = "Miembro del equipo"

    name = fields.char(string="Nombre",required=True)
    rol = fields.char(string="Rol (modulo)", required=True)
    description = fields.Text(string = "Descripcion")
    foto = fields.Image(string="Fotografia")