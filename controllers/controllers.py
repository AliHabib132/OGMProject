# -*- coding: utf-8 -*-
# from odoo import http


# class OgmProject(http.Controller):
#     @http.route('/ogm_project/ogm_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ogm_project/ogm_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ogm_project.listing', {
#             'root': '/ogm_project/ogm_project',
#             'objects': http.request.env['ogm_project.ogm_project'].search([]),
#         })

#     @http.route('/ogm_project/ogm_project/objects/<model("ogm_project.ogm_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ogm_project.object', {
#             'object': obj
#         })
