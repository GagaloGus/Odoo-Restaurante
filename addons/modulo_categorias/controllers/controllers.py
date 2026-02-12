# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloCategorias(http.Controller):
#     @http.route('/modulo_categorias/modulo_categorias', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_categorias/modulo_categorias/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_categorias.listing', {
#             'root': '/modulo_categorias/modulo_categorias',
#             'objects': http.request.env['modulo_categorias.modulo_categorias'].search([]),
#         })

#     @http.route('/modulo_categorias/modulo_categorias/objects/<model("modulo_categorias.modulo_categorias"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_categorias.object', {
#             'object': obj
#         })

