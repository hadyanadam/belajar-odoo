from odoo import models, fields, api, _


class TambahEkstrakurWizard(models.TransientModel):
    _name = "sekolah_custom.tambah_ekstrakur_wizard"
    _description = "Tambah Ekstrakurikuler"

    nama = fields.Many2one(
        "sekolah_custom.ekstrakur", string="Ekstrakurikuler", required=True
    )

    def tambah_ekstrakur(self):
        siswa_ids = self.env.context.get("active_ids", False)
        ekstrakur = self.env["sekolah_custom.ekstrakur"].browse(self.nama.id)
        ekstrakur.write({"siswa": siswa_ids})

    def tambah_ekstrakur_form(self):
        return {
            "type": "ir.actions.act_window",
            "name": _("Tambah Ekstrakur"),
            "res_model": "sekolah_custom.tambah_ekstrakur_wizard",
            "target": "new",
            "view_id": self.env.ref(
                "sekolah_custom.sekolah_custom_tambah_ekstrakur_wizard_form"
            ).id,
            "view_mode": "form",
            "context": self.env.context,
        }
