# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ModuloCategorias(http.Controller):
     @http.route('/categorias', auth='public', website=True)
     def categorias_list(self, **kwargs):
         
        categorias = request.env['restaurante.categoria'].sudo().search([('active', '=', True)])

        return request.render('modulo_categorias.template_categorias', {
            'categorias': categorias
        })