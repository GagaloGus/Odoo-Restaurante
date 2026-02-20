# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class RestauranteWebsite(http.Controller):

    @http.route('/', auth='public', website=True)
    def homepage(self, **kwargs):
        return request.render('modulo_home.homepage')