{
    'name': 'Waterhole',
    'version': '1.0',
    'author': 'Humanytek',
    'website': 'http://humanytek.com',
    'depends': ['purchase', 'purchase_contract_type'],
    'data': [
        'security/ir.model.access.csv',
        'security/waterhole_access_rules.xml',
        'views/waterhole.xml',
        "views/purchase_waterhole.xml",
    ]
}
