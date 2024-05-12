from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    pos_hide_receipt_price = fields.Boolean(
        string="Hide Prices in Receipt",
        help="If checked, prices will be hidden in the receipt generated from Point of Sale.",
    )
