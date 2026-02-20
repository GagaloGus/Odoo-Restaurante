#-*- coding: utf-8 -*-
from odoo import http
from odoo.http import request



class ModuloEquipo(http.Controller):
     @http.route('/equipo', auth='public', website=True)
     def equipo_list(self, **kw):
        miembros = request.env['equipo.miembro'].sudo().search([])
        return request.render('modulo_equipos.web_equipo_list', {
             'miembros': miembros
        })

     @http.route('/equipo/<model("equipo.miembro"):miembro>', auth='public', website=True)
     def equipo_detail(self, miembro, **kw):
         return http.request.render('modulo_equipos.web_equipo_detail', {
             'miembro': miembro
         })

