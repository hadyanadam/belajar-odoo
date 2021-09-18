from odoo import models, fields, _


class UbahKelasWizard(models.TransientModel):
    _name = "ubah_kelas.wizard"
    _description = "Ubah Kelas Wizard"

    kelas = fields.Selection(
        [
            ("I", "I"),
            ("II", "II"),
            ("III", "III"),
        ],
        string="Kelas",
        required=True,
    )

    def ubah_kelas(self):
        siswa_records = self.env["sekolah.siswa"].browse(
            self.env.context.get("active_ids", False)
        )
        for siswa in siswa_records:
            siswa.write({"kelas": self.kelas})

    def ubah_kelas_form(self):
        return {
            "type": "ir.actions.act_window",
            "name": _("Ubah Kelas"),
            "res_model": "ubah_kelas.wizard",
            "target": "new",
            "view_id": self.env.ref("sekolah.ubah_kelas_view_form").id,
            "view_mode": "form",
            "context": self.env.context,
        }
