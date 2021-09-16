# -*- coding: utf-8 -*-

try:
    import qrcode
except ImportError:
    qrcode = None
try:
    import base64
except ImportError:
    base64 = None
from io import BytesIO

from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _compute_amount_to_word(self):
        for rec in self:
            rec.num_in_word = str(rec.currency_id.amount_to_text(rec.amount_total))

    num_in_word = fields.Char(string="Amount In Words:", compute='_compute_amount_to_word')
    qr = fields.Binary(string="QR Code", compute='generate_qr')

    @api.depends('name')
    def generate_qr(self):
        if qrcode and base64:
            if self.name:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(self.name)
                qr.make(fit=True)
                img = qr.make_image()
                temp = BytesIO()
                img.save(temp, format="PNG")
                qr_image = base64.b64encode(temp.getvalue())
                self.write({'qr': qr_image})
