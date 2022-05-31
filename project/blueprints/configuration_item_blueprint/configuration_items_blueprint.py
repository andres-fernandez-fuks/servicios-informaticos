from flask import Blueprint, jsonify
from project.controllers.configuration_item_controller.hardware_ci_controller import HardwareConfigurationItemController
from project.controllers.configuration_item_controller.software_ci_controller import SoftwareConfigurationItemController
from project.controllers.configuration_item_controller.sla_ci_controller import SLAConfigurationItemController
from project.schemas.schemas import ConfigurationItemSchema


CONFIGURATION_ITEMS_ENDPOINT = "/configuration-items"

ci_blueprint = Blueprint("ci_blueprint", __name__)

# item_schema = ConfigurationItemSchema(only=["name", "id", "item_class"])
items_schema = ConfigurationItemSchema(many=True, only=["name", "id", "item_class"])

@ci_blueprint.route(f"{CONFIGURATION_ITEMS_ENDPOINT}/names", methods=["GET"])
def get_configuration_items():
    """
    GET endpoint to get all Hardware Configuration Items
    """
    hardware_conf_items = HardwareConfigurationItemController.load_all()
    software_conf_items = SoftwareConfigurationItemController.load_all()
    sla_conf_items = SLAConfigurationItemController.load_all()
    conf_items = hardware_conf_items + software_conf_items + sla_conf_items
    dump = items_schema.dump(conf_items)
    name_list = {"items": [{"name": item["name"], "value": item["name"]} for item in dump]}
    return jsonify(name_list)