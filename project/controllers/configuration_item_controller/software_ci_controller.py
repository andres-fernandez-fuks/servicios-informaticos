from project.controllers.configuration_item_controller.configuration_item_controller import (
    ConfigurationItemController,
)
from project.models.comment import SoftwareItemComment
from project.models.configuration_item.software_configuration_item import (
    SoftwareConfigurationItem,
)
from project import db
from project.models.versions.software_item_version import SoftwareItemVersion


class SoftwareConfigurationItemController(ConfigurationItemController):
    object_class = SoftwareConfigurationItem
    null_object_class = None
    object_version_class = SoftwareItemVersion
    comment_class = SoftwareItemComment

