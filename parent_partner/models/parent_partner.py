# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ParentPartner(models.Model):
    _inherit = 'res.partner'

    partner_id = fields.Many2one('res.partner', string='Parent')
    # model_id = fields.Many2one('fleet.vehicle.model', string='Model')
    # brand_id = fields.Many2one('fleet.vehicle.model.brand', string='Brand')

    # @api.onchange('partner_id')
    # def onchange_partner(self):
    #     self.company_type = 'company'

    @api.onchange('partner_id')
    def onchange_partner(self):
        self.partner_id.company_type = 'company'

    @api.constrains('name')
    def No_parent(self):
        if self.partner_id:
            partner = self.env['res.partner'].search([('partner_id.name', '=', self.name)])
            if partner:
                raise UserError('Parent Company Cannot be selected as a Child Company')

    def write(self, vals):
        rec = super(ParentPartner, self).write(vals)
        if self.partner_id:
            partner = self.env['res.partner'].search([('partner_id.name', '=', self.name)])
            if partner:
                raise UserError('Parent Company Cannot be selected as a Child Company')
        return rec


class AccountMove(models.Model):
    _inherit = 'account.move'

    parent_partner_id = fields.Many2one('res.partner', string='Parent')

    @api.onchange('partner_id')
    def onchange_partner(self):
        self.parent_partner_id = self.partner_id.partner_id
