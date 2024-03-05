{
    'name':'stock transport',
    'author':'Kash',

    'depends':[
        'stock_picking_batch',
        'fleet',
    ],

    'data':[
        'views/inherit_fleet_category_view.xml',
        'views/inherit_batch_transfer_view.xml',
        'views/inherit_stock_picking_view.xml',
    ],

    'license':'LGPL-3',
}