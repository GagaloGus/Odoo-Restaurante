# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class ModuloReservas(http.Controller):

    @http.route('/reservas', auth='public', website=True)
    def reservas_list(self, **kwargs):
        reservas = request.env['modulo_reservas.modulo_reservas'].sudo().search([])
        return request.render('modulo_reservas.reservas_template', {
            'reservas': reservas
        })

