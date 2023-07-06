from datetime import timedelta
from odoo import models, fields, api

class ExpiredDocumentsReport(models.AbstractModel):
    _name = 'report.fleet.expired_documents_report'
    _description = 'Expired Documents Report'

    doc_ids = fields.Many2many('fleet.documents', string='Documents', compute='_compute_doc_ids')

    @api.depends('doc_ids.notify_expiry')
    def _compute_doc_ids(self):
        for record in self:
            documents = self.env['fleet.documents'].search([
                ('expiry_date', '!=', False),
                ('expiry_date', '<=', fields.Date.today() + timedelta(days=30)),
                ('notify_expiry', '=', True)
            ])
            record.doc_ids = documents
