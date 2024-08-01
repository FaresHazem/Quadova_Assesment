from odoo import fields, models


# Define a new model named "event.event"
class EventEvent(models.Model):
    # Set the mandatory variable for a new class (_name) and set the optional variable (_description)
    _name = "event.event"
    _description = "Event Event"

    # Define a Char field for the event name
    name = fields.Char()

    # Define a Date field for the event date
    date = fields.Date()

    # Define a Char field for the event location
    location = fields.Char()

    # Define a Text field for the event description
    description = fields.Text()
