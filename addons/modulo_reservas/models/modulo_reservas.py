# -*- coding: utf-8 -*-

from odoo import models, fields

class modulo_reservas(models.Model):
    _name = 'modulo_reservas.modulo_reservas'
    _description = 'Reservas'

    name = fields.Char(string="Reserva a nombre de", required=True)
    fecha_reserva = fields.Datetime(string="Fecha y hora de la reserva", required=True)
    fecha_reserva_actualizada = fields.Datetime(string = "Fecha actualizada")
    n_personas  = fields.Integer(string="Numero de comensales")
    description = fields.Text(string="Descripción")