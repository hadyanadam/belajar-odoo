from odoo import fields, models, _, api


class GenerateEvaluasiWizard(models.TransientModel):
    _name = "sekolah_custom.generate_evaluasi_wizard"
    _description = "Generate Evaluasi Wizard"

    ekstrakur = fields.Many2one("sekolah_custom.ekstrakur", string="Ekstrakurikuler")
    trainer = fields.Many2one("sekolah_custom.trainer", string="Trainer", required=True)
    evaluasi_det = fields.One2many(
        "sekolah_custom.evaluasi_det_transient", "evaluasi_id"
    )

    def generate_evaluasi(self):
        eval_det_ids = []
        for rec in self.evaluasi_det:
            eval_det = self.env["sekolah_custom.evaluasi_det"].create(
                {
                    "siswa_id": rec.siswa_id.id,
                    "nilai": rec.nilai,
                }
            )
            eval_det_ids.append(eval_det.id)
        evaluasi = self.env["sekolah_custom.evaluasi"].create(
            {
                "ekstrakur_id": self.ekstrakur.id,
                "trainer_id": self.trainer.id,
                "evaluasi_det": eval_det_ids,
            }
        )

        return {
            "name": _("Evaluasi Form"),
            "type": "ir.actions.act_window",
            "res_model": "sekolah_custom.evaluasi",
            "view_mode": "form",
            "res_id": evaluasi.id,
            "target": "current",
            "view_id": self.env.ref("sekolah_custom.evaluasi_view_form").id,
        }

    def generate_evaluasi_form(self):
        context = dict(self.env.context)
        ekstrakur = self.env[context.get("active_model", False)].browse(
            context.get("active_ids", False)
        )

        eval_det_ids = []
        for id in ekstrakur.siswa.ids:
            evaluasi_det = self.env["sekolah_custom.evaluasi_det_transient"].create(
                {"siswa_id": id, "nilai": 0}
            )
            eval_det_ids.append(evaluasi_det.id)

        context.update(
            {"default_ekstrakur": ekstrakur.id, "default_evaluasi_det": eval_det_ids}
        )
        return {
            "type": "ir.actions.act_window",
            "name": _("Generate Evaluasi"),
            "res_model": "sekolah_custom.generate_evaluasi_wizard",
            "target": "new",
            "view_id": self.env.ref(
                "sekolah_custom.generate_evaluasi_wizard_view_form"
            ).id,
            "view_mode": "form",
            "context": context,
        }


class EvaluasiDetTransient(models.TransientModel):
    _name = "sekolah_custom.evaluasi_det_transient"

    evaluasi_id = fields.Many2one(
        "sekolah_custom.generate_evaluasi_wizard", string="Evaluasi", default=False
    )
    siswa_id = fields.Many2one("sekolah.siswa", string="Siswa")
    nilai = fields.Float("Nilai")
