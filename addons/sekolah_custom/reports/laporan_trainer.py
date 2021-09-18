from odoo import api, models


class LaporanTrainer(models.AbstractModel):
    _name = "report.sekolah_custom.laporan_trainer"

    def _get_report_values(self, docids, data=None):
        docs = []
        for id in docids:
            doc = self.env["sekolah_custom.evaluasi"].search([("trainer_id", "=", id)])
            docs.append((doc[0].trainer_id.nama, doc))

        return {
            "doc_ids": docids,
            "doc_model": "sekolah_custom.evaluasi",
            "docs": docs,
            "data": data,
        }
