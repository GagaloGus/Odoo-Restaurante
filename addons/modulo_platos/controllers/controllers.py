# -*- coding: utf-8 -*-
from odoo import http # type: ignore
from odoo.http import request # type: ignore

class ModuloPlatos(http.Controller):
    @http.route('/carta', auth='public', website=True)
    def mostrar_carta(self, **kw):
        carta = request.env['modulo_platos.plato'].sudo().search([])
        return request.render('modulo_platos.web_platos_list', {
            'carta': carta
        })
    
    @http.route('/carta/<model("modulo_platos.plato"):plato>', auth='public', website=True)
    def productos_detalles(self, plato, **kw):
        return request.render('modulo_platos.web_plato_detail', {
            'plato': plato
        })
