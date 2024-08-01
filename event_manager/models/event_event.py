from odoo import fields, models


class EventEvent(models.Model):
    _name = "event.event"
    _description = "Event Event"

    name = fields.Char()
    date = fields.Date()
    location = fields.Char()
    description = fields.Text()
