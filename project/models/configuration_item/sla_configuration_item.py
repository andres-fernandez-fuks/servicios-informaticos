from sqlalchemy import ForeignKey
from project.models.configuration_item.configuration_item import ConfigurationItem
from project import db


class SLAConfigurationItem(ConfigurationItem):
    __tablename__ = "ci_sla"

    current_version_id = db.Column(db.Integer, ForeignKey("item_sla_version.id"), nullable=True)
    # nullable True xq el ítem se crea antes que la primera versión
    draft_id = db.Column(db.Integer, ForeignKey("item_sla_version.id"), nullable=True)
    versions = db.relationship("SLAItemVersion", backref="configuration_item", lazy=True, foreign_keys="SLAItemVersion.item_id")
    current_version = db.relationship("SLAItemVersion", foreign_keys=[current_version_id])
    draft = db.relationship("SLAItemVersion", foreign_keys=[draft_id])

    def __init__(self, current_version_id: int = None, **kwargs):
        super().__init__("SLA")
        self.current_version_id = current_version_id
        self.draft_id = None

    
    