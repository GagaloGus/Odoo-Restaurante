# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloPlatos(http.Controller):
#     @http.route('/modulo_platos/modulo_platos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_platos/modulo_platos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_platos.listing', {
#             'root': '/modulo_platos/modulo_platos',
#             'objects': http.request.env['modulo_platos.modulo_platos'].search([]),
#         })

#     @http.route('/modulo_platos/modulo_platos/objects/<model("modulo_platos.modulo_platos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_platos.object', {
#             'object': obj
#         })

