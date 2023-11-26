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
    'depends': ['base', 'website', 'website_sale', 'website_sale_stock', 'account', 'stock', 'contacts'],

    'installable': True,

    'application': True,

    # always loaded
    'data': [
        'views/landing_page.xml',
        # 'views/footer.xml',
        'data/res.partner.csv',
        'data/res.company.csv',
        'data/res.lang.xml',
        'data/website.xml',
        'data/website.page.csv',
        'data/product.template.csv',
        'data/res.users.csv',
        'data/res.groups.xml',
        'data/website.page.sql',
        'data/no_update.sql',
    ],

    'assets': {
        'web.assets_frontend': [
            'victorikus_web/static/src/js/landing_page.js',
            'victorikus_web/static/src/css/styles.css',
        ],
    },

    # only loaded in demonstration mode
    'demo': [
    ],
}
