# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ModuloCategorias(http.Controller):
     @http.route('/categorias', auth='public', website=True)
     def categorias_list(self, **kwargs):
         return "Hello, world"