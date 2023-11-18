# -*- coding: utf-8 -*-
{
    'name': "Victorikus Web",

    'summary': """
        Cake Shop Website.
        """,

    'description': """
    Cake Shop Website.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'license': 'Other proprietary',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'website_sale', 'website_sale_stock', 'account', 'stock'],

    'installable': True,

    'application': True,

    # always loaded
    'data': [
        'data/res.partner.csv',
        'data/res.company.csv',
        'views/home_page.xml',
        'data/res.lang.csv',
        'data/website.csv',
        'data/website.page.sql',
        'data/website.page.csv',
        'data/product.template.csv',
        'data/res.users.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
