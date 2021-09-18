from odoo import models, fields


class Evaluasi(models.Model):
    _name = "sekolah_custom.evaluasi"
    _description = "Evaluasi"

    ekstrakur_id = fields.Many2one("sekolah_custom.ekstrakur", string="Ekstrakurikuler")
    trainer_id = fields.Many2one("sekolah_custom.trainer", string="Trainer")
    rata_rata = fields.Float("Rata-rata", compute="_compute_rata_rata")
    evaluasi_det = fields.One2many(
        "sekolah_custom.evaluasi_det", "evaluasi_id", string="Evaluasi Det"
    )

    def name_get(self):
        names = []
        for rec in self:
            names.append((rec.id, f"Evaluasi {rec.ekstrakur_id.nama}"))
        return names

    def _compute_rata_rata(self):
        for rec in self:
            if len(rec.evaluasi_det):
                rec.rata_rata = sum(rec.nilai for rec in rec.evaluasi_det) / len(
                    rec.evaluasi_det
                )
            else:
                rec.rata_rata = 0
