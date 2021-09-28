# -*- coding: utf-8 -*-
{
    'name': "Parent Partner",

    'summary': """
        Make A Field on Partner Form and Show Under The Address Type""",

    'description': """
        Make A Field on Partner Form and Show Under The Address Type
    """,

    'author': "Viltco",
    'website': "http://www.viltco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'contacts',
    'version': '14.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'account','account_reports'],

    # always loaded
    'data': [
        'views/parent_partner_views.xml',
    ],

}
