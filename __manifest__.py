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
    'depends': ['base', 'pasar', 'website', 'web', 'website_blog'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/web_home.xml',
        'views/web_pendaftaran.xml',
        'views/web_pembaruan.xml',
        'views/web_denah.xml',
        'views/web_visimisi.xml',
        'views/web_infokomoditas.xml',
        'views/web_pasaragrobisbabat.xml',
        'views/web_pasarbabat.xml',
        'views/web_pasarbarulamongan.xml',
        'views/web_blog_page.xml',
        'views/web_root.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        'static/src/xml/web_home.xml',
        'static/src/xml/web_pendaftaran.xml',
        'static/src/xml/web_pembaruan.xml',
        'static/src/xml/web_denah.xml',
        'static/src/xml/web_pasarbarulamongan.xml',
        'static/src/xml/web_pasarbabat.xml',
        'static/src/xml/web_pasaragrobisbabat.xml',

    ],
    'images': [
        'images/bg_1.jpg'
    ],
    'css': [
        '/web_simpasar/static/src/xml/css/ajax-loader.gif',
        '/web_simpasar/static/src/xml/css/animate.css',
        '/web_simpasar/static/src/xml/css/bootstrap.min.css',
        '/web_simpasar/static/src/xml/css/flaticon.css',
        '/web_simpasar/static/src/xml/css/magnific-popup.css',
        '/web_simpasar/static/src/xml/css/owl.carousel.min.css',
        '/web_simpasar/static/src/xml/css/owl.theme.default.min.css',
        '/web_simpasar/static/src/xml/css/style.css',
        '/web_simpasar/static/src/xml/css/css/bootstrap-reboot.css',
        '/web_simpasar/static/src/xml/css/css/mixins/_text-hide.css',
        '/web_simpasar/static/src/xml/css/bootstrap/mixins/bootstrap-grid.css',
        '/web_simpasar/static/src/xml/css/bootstrap/mixins/bootstrap-reboot.css',
        '/web_simpasar/static/src/xml/fonts/flaticon/font/_flaticon.scss',
        '/web_simpasar/static/src/xml/fonts/flaticon/font/flaticon.css',
        '/web_simpasar/static/src/xml/fonts/flaticon/font/Flaticon.eot',
        '/web_simpasar/static/src/xml/fonts/flaticon/font/Flaticon.svg',
        '/web_simpasar/static/src/xml/fonts/flaticon/font/Flaticon.woff',
        '/web_simpasar/static/src/xml/fonts/flaticon/font/Flaticon.woff2',
    ],

    #web_asset
    'web.assets_frontend': [
        '/web_simpasar/static/src/js/main.js',
        '/web_simpasar/static/src/xml/js/bootsrap.min.js',
        '/web_simpasar/static/src/xml/js/google-maps.js',
        '/web_simpasar/static/src/xml/js/jquery-3.2.1.min.js',
        '/web_simpasar/static/src/xml/js/jquery-migrate-3.0.1.min.js',
        '/web_simpasar/static/src/xml/js/jquery.animateNumber.min.js',
        '/web_simpasar/static/src/xml/js/jquery.easing.1.3.js',
        '/web_simpasar/static/src/xml/js/jquery.magnific-popup.min.js',
        '/web_simpasar/static/src/xml/js/jquery.min.js',
        '/web_simpasar/static/src/xml/js/jquery.stellar.min.js',
        '/web_simpasar/static/src/xml/js/jquery.waypoints.min.js',
        '/web_simpasar/static/src/xml/js/main.js',
        '/web_simpasar/static/src/xml/js/owl.carousel.min.js',
        '/web_simpasar/static/src/xml/js/popper.min.js',
        '/web_simpasar/static/src/xml/js/scrollax.min.js',
        '/web_simpasar/static/src/xml/scss/style.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_alert.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_badge.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_breadcrumb.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_button-group.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_buttons.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_card.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_carousel.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_close.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_code.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_custom-forms.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_dropdown.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_forms.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_functions.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_grid.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_images.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_input-group.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_jumbotron.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_list-group.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_media.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_mixins.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_modal.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_nav.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_navbar.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_pagination.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_popover.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_print.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_progress.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_reboot.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_root.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_spinners.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_tables.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_toasts.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_tooltip.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_transitions.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_type.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_utilities.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/_variables.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/bootstrap-gird.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/bootstrap-reboot.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/bootstrap.scss',
        '/web_simpasar/static/src/xml/scss/bootstrap/utilities',
        '/web_simpasar/static/src/xml/scss/bootstrap/mixins',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
