from odoo import models, fields, api


class UjianDet(models.Model):
    _name = "sekolah.ujian_det"
    _description = "Ujian"

    ujian_id = fields.Many2one("sekolah.ujian")
    mata_pelajaran_id = fields.Many2one("sekolah.mata_pelajaran")
    nilai = fields.Float()

    def name_get(self):
        names = []
        for rec in self:
            names.append((rec.id, f"{rec.mata_pelajaran_id.nama} - {rec.nilai}"))
        return names