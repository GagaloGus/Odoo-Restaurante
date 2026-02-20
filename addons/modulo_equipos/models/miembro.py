from odoo import models, fields

class EquipoMiembro(models.Model):
    _name = "equipo.miembro"
    _description = "Miembro del equipo"

    name = fields.Char(string="Nombre", required=True)
    rol = fields.Char(string="Rol (modulo)", required=True)
    description = fields.Text(string = "Descripcion")
    foto = fields.Image(string="Fotografia")