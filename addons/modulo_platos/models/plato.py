# -*- coding: utf-8 -*-
from odoo import models, fields, api  # type: ignore

class Plato(models.Model):
    _name = 'modulo_platos.plato'
    _description = 'Platos del Restaurante'

    name = fields.Char('Nombre', required=True)
    #default_code = fields.Char('Referencia')
    price = fields.Float('Precio')
    description = fields.Text('Descripción')
    available = fields.Boolean('Disponible', default=True)
    image = fields.Image('Imagen')