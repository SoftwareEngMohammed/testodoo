# -*- coding: utf-8 -*-
{
    'name': "My task",
    'summary': """
       this task to add fields in inventory  """,
    'description': """
        this task to add fields in inventory
    """,
    'author': "Muhamed Ashraf",
    'website': "https://github.com/SoftwareEngMohammed",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','stock','product'],
    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
        # 'views/customeview.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
'installable':True,
'auto_install':False,
'application':True,
}
