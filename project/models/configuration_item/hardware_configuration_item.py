from sqlalchemy import ForeignKey
from project.models.configuration_item.configuration_item import ConfigurationItem
from project import db


class HardwareConfigurationItem(ConfigurationItem):
    __tablename__ = "ci_hardware"

    current_version_id = db.Column(
        db.Integer, ForeignKey("item_hardware_version.id"), nullable=True
    )
    # nullable True xq el ítem se crea antes que la primera versión
    draft_id = db.Column(
        db.Integer, ForeignKey("item_hardware_version.id"), nullable=True
    )
    versions = db.relationship(
        "HardwareItemVersion",
        foreign_keys="HardwareItemVersion.item_id",
        cascade="all, delete-orphan",
    )
    current_version = db.relationship(
        "HardwareItemVersion", foreign_keys=[current_version_id]
    )
    draft = db.relationship("HardwareItemVersion", foreign_keys=[draft_id])

    def __init__(self, current_version_id: int = None, **kwargs):
        super().__init__("Hardware")
        self.current_version_id = current_version_id
        self.draft_id = None

