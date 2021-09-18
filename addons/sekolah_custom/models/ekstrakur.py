from odoo import models, fields, api


class Ekstrakur(models.Model):
    _name = "sekolah_custom.ekstrakur"
    _description = "Ekstrakulikuler"

    nama = fields.Char("Nama Ekstrakurikuler")
    siswa = fields.Many2many(
        "sekolah.siswa",
        "siswa_ekstrakur_rel",
        "ekstrakur_id",
        "siswa_id",
        string="Siswa",
    )

    def name_get(self):
        names = []
        for rec in self:
            names.append((rec.id, rec.nama))
        return names


class Siswa(models.Model):
    _inherit = "sekolah.siswa"

    ekstrakur = fields.Many2many(
        "sekolah_custom.ekstrakur",
        "siswa_ekstrakur_rel",
        "siswa_id",
        "ekstrakur_id",
        string="Ekstrakurikuler",
    )
