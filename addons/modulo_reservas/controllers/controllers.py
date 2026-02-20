# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from zoneinfo import ZoneInfo

class ModuloReservas(http.Controller):

    @http.route('/reservas', auth='public', website=True)
    def reservas_list(self, **kwargs):
        reservas = request.env['modulo_reservas.modulo_reservas'].sudo().search([])

        for r in reservas:
            dt = r.fecha_reserva
            dt_madrid = dt.astimezone(ZoneInfo('Europe/Madrid'))
            r.fecha_reserva_actualizada = dt_madrid.replace(tzinfo=None)

        return request.render('modulo_reservas.reservas_template', {
            'reservas': reservas
        })

