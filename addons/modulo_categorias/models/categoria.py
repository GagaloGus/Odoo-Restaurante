from odoo import models, fields

class Categoria(models.Model):
    _name = "restaurante.categoria"
    _description = "Categorias del Restaurante"

    name = fields.Char(string = "Nombre", required=True)
    description = fields.Text(string = "Descripción")
    active = fields.Boolean(string = "Activo")
    # imagen = fields.Binary(string = "Imagen")