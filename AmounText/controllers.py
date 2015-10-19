# -*- coding: utf-8 -*-
from openerp import http

# class Gesimport(http.Controller):
#     @http.route('/gesimport/gesimport/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gesimport/gesimport/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gesimport.listing', {
#             'root': '/gesimport/gesimport',
#             'objects': http.request.env['gesimport.gesimport'].search([]),
#         })

#     @http.route('/gesimport/gesimport/objects/<model("gesimport.gesimport"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gesimport.object', {
#             'object': obj
#         })