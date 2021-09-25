# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ParentPartner(models.Model):
    _inherit = 'res.partner'

    partner_id = fields.Many2one('res.partner', string='Parent')

    def get_parent_id_custom_m20_val(self):
        custom_m20 = []
        partner_ids = self.env['res.partner'].sudo().search([('partner_id','=',False)])
        for partner_id in partner_ids:
            child_id = self.env['res.partner'].sudo().search([('partner_id','=',partner_id.id)])
            if child_id:
                custom_m20.append(partner_id.id)
        return custom_m20

    @api.onchange('partner_id')
    def onchange_partner(self):
        self.partner_id.company_type = 'company'

class AccountMove(models.Model):
    _inherit = 'account.move'

    parent_partner_id = fields.Many2one('res.partner', string='Parent')

    @api.onchange('partner_id')
    def onchange_partner(self):
        self.parent_partner_id = self.partner_id.partner_id

class AccountReportDA(models.AbstractModel):
    _inherit = 'account.report'

    def get_report_only_parent_ids(self,p_ids=False):
        parent_id = []
        if p_ids:
            child_id = self.env['res.partner'].sudo().search([('partner_id','=',int(p_ids))])
            for j in child_id:
                val = {'name':j.name,'id':j.id}
                parent_id.append(val)
        return parent_id

    @api.model
    def _init_filter_partner(self, options, previous_options=None):
        res = super(AccountReportDA, self)._init_filter_partner(options=options,previous_options=previous_options)
        if self.filter_partner and self._name == 'account.partner.ledger':
            options['parent_id_custom_m20'] = previous_options and previous_options.get('parent_id_custom_m20') or False
        return res
