from odoo import models, fields


class MataPelajaran(models.Model):
    _name = "sekolah.mata_pelajaran"
    _description = "Mata Pelajaran"

    nama = fields.Char(string="Nama Pelajaran", required=True)

    def name_get(self):
        names = []
        for rec in self:
            names.append((rec.id, rec.nama))
        return names