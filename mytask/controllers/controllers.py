# -*- coding: utf-8 -*-
# from odoo import http


# class Mytask(http.Controller):
#     @http.route('/mytask/mytask/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mytask/mytask/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mytask.listing', {
#             'root': '/mytask/mytask',
#             'objects': http.request.env['mytask.mytask'].search([]),
#         })

#     @http.route('/mytask/mytask/objects/<model("mytask.mytask"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mytask.object', {
#             'object': obj
#         })
