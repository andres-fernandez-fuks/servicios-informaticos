from flask import Blueprint, jsonify, request
from project.controllers.incident_controller import IncidentController
from project.schemas.schemas import IncidentSchema

INCIDENTS_ENDPOINT = "/incidents"

incident_blueprint = Blueprint("incidents_blueprint", __name__)
incident_schema = IncidentSchema()
incidents_schema = IncidentSchema(many=True)


@incident_blueprint.route(f"{INCIDENTS_ENDPOINT}", methods=["GET"])
# @user_required([EDIT_DISTRIBUTOR])
def get_incidents():
    """
    GET endpoint to get all Incidents.
    """
    incidents = IncidentController.load_all()
    return jsonify(incidents_schema.dump(incidents))

@incident_blueprint.route(f"{INCIDENTS_ENDPOINT}/<user_id>", methods=["GET"])
# @user_required([EDIT_DISTRIBUTOR])
def get_user_incidents(user_id):
    """
    GET endpoint to get all Incidents from a specific user.
    """
    incidents = IncidentController.load_incidents_assigned_to_user(username=user_id)
    return jsonify(incidents_schema.dump(incidents))

@incident_blueprint.route(f"{INCIDENTS_ENDPOINT}/assigned", methods=["GET"])
# @user_required([EDIT_DISTRIBUTOR])
def get_assigned_incidents():
    """
    GET endpoint to get all Incidents.
    """
    incidents = IncidentController.load_assigned_incidents()
    return jsonify(incidents_schema.dump(incidents))

@incident_blueprint.route(f"{INCIDENTS_ENDPOINT}/not-assigned", methods=["GET"])
# @user_required([EDIT_DISTRIBUTOR])
def get_unassigned_incidents():
    """
    GET endpoint to get all Incidents.
    """
    incidents = IncidentController.load_unassigned_incidents()
    return jsonify(incidents_schema.dump(incidents))


@incident_blueprint.route(f"{INCIDENTS_ENDPOINT}", methods=["POST"])
# @user_required([EDIT_DISTRIBUTOR])
def create_incident():
    """
    POST endpoint to create a new Incident.
    """
    #new_incident = incident_schema.load(request.json)
    incident = IncidentController.create(**request.json)
    return incident_schema.dump(incident)


@incident_blueprint.route(f"{INCIDENTS_ENDPOINT}/<incident_id>", methods=["DELETE"])
# @user_required([EDIT_DISTRIBUTOR])
def delete_incident(incident_id):
    """
    DELETE endpoint to delete a given Incident.
    """
    incident = IncidentController.load_by_id(incident_id)
    try:
        IncidentController.delete(incident)
    except Exception as e:
        return jsonify({"error": str(e)}), 404


@incident_blueprint.route(f"{INCIDENTS_ENDPOINT}/all", methods=["DELETE"])
# @user_required([EDIT_DISTRIBUTOR])
def delete_all():
    """
    DELETE endpoint to delete all Incidents.
    """
    incidents_amount = IncidentController.count()
    IncidentController.delete_all()
    return f"{incidents_amount} incidents have been deleted"
