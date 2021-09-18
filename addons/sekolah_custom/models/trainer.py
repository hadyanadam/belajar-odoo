from odoo import models, fields


class Trainer(models.Model):
    _name = "sekolah_custom.trainer"
    _description = "Trainer"

    nama = fields.Char("Nama Trainer", required=True)

    def name_get(self):
        names = []
        for rec in self:
            names.append((rec.id, rec.nama))
        return names

    def laporan_trainer(self):
        docids = self.env.context.get("active_ids")
        return self.env.ref("sekolah_custom.laporan_trainer_report").report_action(
            docids
        )
