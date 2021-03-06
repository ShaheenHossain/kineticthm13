{
    "name": """Email Addresses and Templates per Website""",
    "summary": """Use single Backend to manage several Websites""",
    "category": "Discuss",
    "images": ["images/main.jpg"],
    "version": "13.0.1.0.1",
    "application": True,
    "depends": [
        "ir_config_parameter_multi_company",
        "web_website",
        "mail",
        "test_mail",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/website_views.xml"],
    "demo": [],
    "qweb": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
    "auto_install": False,
    "installable": True,
    # "demo_title": "Email Addresses per Website",
    # "demo_addons": [
    # ],
    # "demo_addons_hidden": [
    # ],
    # "demo_url": "DEMO-URL",
    # "demo_summary": "Use single Backend to manage several Websites",
    # "demo_images": [
    #    "images/MAIN_IMAGE",
    # ]
}
