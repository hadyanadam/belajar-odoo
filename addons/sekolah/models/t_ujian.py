from datetime import datetime, date
from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class Ujian(models.Model):
    _name = "sekolah.ujian"
    _description = "Ujian"

    tgl_ujian = fields.Date(string="Tanggal Ujian")
    siswa_id = fields.Many2one("sekolah.siswa", string="Siswa")
    rata_rata = fields.Float(string="Rata-rata", compute="_compute_rata_rata")
    ujian_det = fields.One2many("sekolah.ujian_det", "ujian_id")

    def name_get(self):
        names = []
        for rec in self:
            names.append((rec.id, f"{rec.tgl_ujian} - {rec.siswa_id.nama}"))
        return names

    def _compute_rata_rata(self):
        for rec in self:
            if len(rec.ujian_det):
                rec.rata_rata = sum(rec.nilai for rec in rec.ujian_det) / len(
                    rec.ujian_det
                )
            else:
                rec.rata_rata = 0

    def _validate_tgl_ujian(self, vals):
        if vals.get("tgl_ujian", False):
            input_tgl_ujian = date.fromisoformat(vals.get("tgl_ujian"))
        else:
            input_tgl_ujian = self.tgl_ujian
        if input_tgl_ujian > date.today():
            raise ValidationError(
                _(f"Tanggal ujian harus <= {datetime.now().strftime('%d %B %Y')}")
            )

    def write(self, vals):
        self._validate_tgl_ujian(vals)
        return super(Ujian, self).write(vals)

    @api.model
    def create(self, vals):
        self._validate_tgl_ujian(vals)
        return super(Ujian, self).create(vals)
