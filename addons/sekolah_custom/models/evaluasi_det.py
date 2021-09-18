from odoo import models, fields, api


class EvaluasiDet(models.Model):
    _name = "sekolah_custom.evaluasi_det"

    evaluasi_id = fields.Many2one(
        "sekolah_custom.evaluasi", string="Evaluasi", default=False
    )
    siswa_id = fields.Many2one("sekolah.siswa", string="Siswa")
    nilai = fields.Float("Nilai")

    def name_get(self):
        names = []
        for rec in self:
            names.append((rec.id, f"{rec.siswa_id} - {rec.nilai}"))
        return names
