{
    'name': 'Sale Discount on Total Amount',
    'version': '1.0',
    'category': 'sale',
    'sequence': 6,
    'summary': "A module meant to provide discount for total amount and Discount limit with approval in sales",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'http://www.cybrosys.com',

    'description': """

Sale Discount for Total Amount
=======================
Module to manage discount on total amount in Sale.
        as an specific amount or percentage
""",
    'depends': ['sale', 'base', 'stock'],
    'data': [
        'views/sale_view.xml',
        'views/account_invoice_view.xml',
        'views/invoice_report.xml',
        'views/sale_order_report.xml',
        'views/sale_discount_approval_view.xml',
        'views/sale_discount_approval_workflow.xml'

    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
}
