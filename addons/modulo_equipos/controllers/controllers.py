# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloEquipos(http.Controller):
#     @http.route('/modulo_equipos/modulo_equipos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_equipos/modulo_equipos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_equipos.listing', {
#             'root': '/modulo_equipos/modulo_equipos',
#             'objects': http.request.env['modulo_equipos.modulo_equipos'].search([]),
#         })

#     @http.route('/modulo_equipos/modulo_equipos/objects/<model("modulo_equipos.modulo_equipos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_equipos.object', {
#             'object': obj
#         })

