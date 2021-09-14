# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ParentPartner(models.Model):
    _inherit = 'res.partner'

    partner_id = fields.Many2one('res.partner', string='Parent')
    model_id = fields.Many2one('fleet.vehicle.model', string='Model')
    brand_id = fields.Many2one('fleet.vehicle.model.brand', string='Brand')


class AccountMove(models.Model):
    _inherit = 'account.move'

    parent_partner_id = fields.Many2one('res.partner', string='Parent')

    @api.onchange('partner_id')
    def onchange_partner(self):
        self.parent_partner_id = self.partner_id.partner_id
