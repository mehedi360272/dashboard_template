# -*- coding: utf-8 -*-
{
    'name': "Dashboard",

    'summary': " ",

    'description': " ",

    'author': " ",
    'website': " ",
    'category': 'Education',
    'version': '16.0.1',

    'depends': [
        'base',
        # 'base_setup',
        # 'mail',
        # 'website',
        # 'smartedu_core',
        # 'web_tour',
        # 'web_kanban_gauge',
    ],

    # always loaded
    'data': [
        'views/dashboard_action.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'dashboard_template/static/src/js/dashboard.js',
            'dashboard_template/static/src/xml/dashboard.xml',
        ],
    },

    'installable': True,
    'auto_install': False,
    'application': True,
    }
