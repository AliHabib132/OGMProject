# -*- coding: utf-8 -*-
{
    'name': "OGM",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ali",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/att_data.xml',
        'views/attendance_view.xml',
        'views/trainee.xml',
        'views/batch.xml',
        'views/task.xml',
        'reports/report_attendance_button.xml',
        'reports/report_attendance_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
