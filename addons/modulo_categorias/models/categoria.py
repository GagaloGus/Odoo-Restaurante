from odoo import models, fields

class Categoria(models.Model):
    _name = "restaurante.categoria"
    _description = "Categorías del Restaurante"

    name = fields.Char(string = "Nombre", required=True)
    description = fields.Tetx(string = "Descripción")
    active = fields.Boolean(string = "Activo")
    imagen = fields.Binary(string = "Imagen")