# -*- coding: utf-8 -*-
{
    "name": "sekolah",
    "summary": """Odoo Learning by creating sekolah app""",
    "author": "My Company",
    "website": "http://www.yourcompany.com",
    "category": "Sistem Sekolah",
    "version": "0.1",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/views.xml",
        "views/siswa_view.xml",
        "views/mata_pelajaran_view.xml",
        "views/t_ujian_view.xml",
        "wizards/ubah_kelas_wizard_view.xml",
    ],
    # only loaded in demonstration mode
    "installable": True,
    "auto_install": False,
    "application": True,
}
