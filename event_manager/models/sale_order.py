from odoo import models, fields


# Inherit the Sale Order model to add a new field
class SaleOrder(models.Model):
    # Specify that this model is an extension of the existing 'sale.order' model
    _inherit = 'sale.order'

    # Define a Many2one relationship field to link a sale order to an event
    event_id = fields.Many2one('event.event', string='Event')  # 'event.event' is the target model, and 'Event' is the field label
