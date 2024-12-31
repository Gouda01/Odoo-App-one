{
    'name': "App One",
    'version': '17.0.0.1.0',
    'depends': ['base', 'mail', 'contacts'],
    'author': "Mohamed Gouda",
    'category': '',

    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/res_partner_view.xml',
        'views/building_view.xml',
    ],
    'assets': {
        'web.assets_backend': ['app_one\static\src\css\property.css']
    },

    'application' : True,

}