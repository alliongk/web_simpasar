# -*- coding: utf-8 -*-
{
    'name': "web_simpasar",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'pasar', 'website', 'web', 'website_sale', 'website_blog', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/web_navbar.xml',
        'views/web_home.xml',
        'views/web_pendaftaran.xml',
        'views/web_pembaruan.xml',
        'views/web_denah.xml',
        'views/web_visimisi.xml',
        'views/web_infokomoditas.xml',
        'views/web_pasaragrobisbabat.xml',
        'views/web_pasarbabat.xml',
        'views/web_pasarbarulamongan.xml',
        'views/web_shopdetail.xml',
        # 'views/web_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            '/pasar/static/src/js/main.js',
            '/web_simpasar/static/src/css/web_pendaftaran.css',
            '/web_simpasar/static/src/css/web_misi.css',
            '/web_simpasar/static/src/css/animasi.css',
            'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css',
        ],
    },

    'installable': True,
    'auto_install': False,
    'application': False,
}
