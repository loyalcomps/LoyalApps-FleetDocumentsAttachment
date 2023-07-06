from datetime import timedelta

from odoo import models, fields,api



class Fleet(models.Model):
    _inherit = 'fleet.vehicle'

    ref = fields.Char(string="Ref:")
    attachments = fields.One2many('fleet.documents', 'fleet_id', string="Attachments")


class FleetDocuments(models.Model):
    _name = 'fleet.documents'
    _description = 'Fleet Attachment'

    name = fields.Char(string="Description")
    attachment = fields.Binary(string="Attachment")
    attachment_name = fields.Char(string="Attachment Name")
    expiry_date = fields.Date(string="Expiry Date")
    notify_expiry = fields.Boolean(string="Notify Expiry")
    fleet_id = fields.Many2one('fleet.vehicle', string="Fleet")

