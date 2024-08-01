{
    "name": "Event Manager",
    "version": "17.0.0.0.0",
    "license": "OEEL-1",
    "depends": ["base", "sale_management"],
    "application": True,
    "data": [
        # SECURITY
        #"security/res_groups.xml",
        "security/ir.model.access.csv",
        # VIEWS
        "views/event_event_views.xml",
        # MENUS
        "views/event_menu.xml",
    ],
}
