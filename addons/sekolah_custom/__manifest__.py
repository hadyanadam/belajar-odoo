# -*- coding: utf-8 -*-
{
    "name": "sekolah_custom",
    "summary": """Odoo Learning by creating sekolah_custom app
                by inherit sekolah module""",
    "author": "My Company",
    "website": "http://www.yourcompany.com",
    "category": "Sistem Sekolah",
    "version": "0.1",
    "depends": ["base", "sekolah"],
    "data": [
        "security/ir.model.access.csv",
        "views/ekstrakur_view.xml",
        "views/trainer_view.xml",
        "views/evaluasi_view.xml",
        "wizards/tambah_ekstrakur_wizard_view.xml",
        "wizards/generate_evaluasi_wizard_view.xml",
        # "reports/laporan_trainer.xml",
        "reports/laporan_trainer_template.xml",
    ],
    # only loaded in demonstration mode
    "installable": True,
    "auto_install": False,
    "application": True,
}
