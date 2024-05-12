# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    pos_hide_receipt_price = fields.Boolean(related='pos_config_id.pos_hide_receipt_price', readonly=False)



