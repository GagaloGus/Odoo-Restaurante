# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloReservas(http.Controller):
#     @http.route('/modulo_reservas/modulo_reservas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_reservas/modulo_reservas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_reservas.listing', {
#             'root': '/modulo_reservas/modulo_reservas',
#             'objects': http.request.env['modulo_reservas.modulo_reservas'].search([]),
#         })

#     @http.route('/modulo_reservas/modulo_reservas/objects/<model("modulo_reservas.modulo_reservas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_reservas.object', {
#             'object': obj
#         })

