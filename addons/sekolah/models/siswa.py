from odoo import models, fields


class Siswa(models.Model):
    _name = "sekolah.siswa"
    _description = "Siswa"

    nama = fields.Char(string="Nama Siswa", required=True)
    kelas = fields.Selection([("I", "I"), ("II", "II"), ("III", "III")], string="Kelas")

    def name_get(self):
        names = []
        for rec in self:
            names.append((rec.id, rec.nama))
        return names
