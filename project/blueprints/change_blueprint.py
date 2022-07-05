from flask import Blueprint, jsonify, request
from project.controllers.change_controller import ChangeController
from project.helpers.change_request_helper import ChangeRequestHelper
from project.helpers.request_helpers import ErrorHandler
from project.schemas.schemas import ChangeSchema

CHANGES_ENDPOINT = "/changes"

change_blueprint = Blueprint("change_blueprint", __name__)


change_schema = ChangeSchema()
changes_schema = ChangeSchema(many=True)


@change_blueprint.route(f"{CHANGES_ENDPOINT}/<change_id>", methods=["GET"])
def get_change(change_id):
    """
    GET endpoint to get all Changes.
    """
    try:
        change = ChangeController.load_by_id(change_id)
        return change_schema.dump(change), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


@change_blueprint.route(f"{CHANGES_ENDPOINT}", methods=["GET"])
def get_changes():
    """
    GET endpoint to get all Changes.
    """
    changes = ChangeController.load_all()
    return jsonify(changes_schema.dump(changes))


@change_blueprint.route(f"{CHANGES_ENDPOINT}/<user_id>", methods=["GET"])
# @user_required([EDIT_DISTRIBUTOR])
def get_user_changes(user_id):
    """
    GET endpoint to get all Changes from a specific user.
    """
    changes = ChangeController.load_assigned_to_user(username=user_id)
    return jsonify(changes_schema.dump(changes))


@change_blueprint.route(f"{CHANGES_ENDPOINT}/assigned", methods=["GET"])
# @user_required([EDIT_DISTRIBUTOR])
def get_assigned_changes():
    """
    GET endpoint to get all Changes.
    """
    changes = ChangeController.load_assigned()
    return jsonify(changes_schema.dump(changes))


@change_blueprint.route(f"{CHANGES_ENDPOINT}/not-assigned", methods=["GET"])
# @user_required([EDIT_DISTRIBUTOR])
def get_unassigned_changes():
    """
    GET endpoint to get all Changes.
    """
    changes = ChangeController.load_unassigned()
    return jsonify(changes_schema.dump(changes))


@change_blueprint.route(f"{CHANGES_ENDPOINT}", methods=["POST"])
# @user_required([EDIT_DISTRIBUTOR])
def create_change():
    """
    POST endpoint to create a new Change.
    """
    try:
        correct_request = ChangeRequestHelper.create_change_request(request.json)
        change = ChangeController.create(**correct_request)
        return change_schema.dump(change)
    except Exception as e:
        return ErrorHandler.determine_http_error_response(e)

@change_blueprint.route(f"{CHANGES_ENDPOINT}/solved", methods=["GET"])
# @user_required([EDIT_DISTRIBUTOR])
def get_solved_incidents():
    """
    GET endpoint to get all Incidents.
    """
    changes = ChangeController.load_solved()
    return jsonify(changes_schema.dump(changes))


@change_blueprint.route(f"{CHANGES_ENDPOINT}/pending", methods=["GET"])
# @user_required([EDIT_DISTRIBUTOR])
def get_pending_incidents():
    """
    GET endpoint to get all Incidents.
    """
    changes = ChangeController.load_pending()
    return jsonify(changes_schema.dump(changes))


@change_blueprint.route(f"{CHANGES_ENDPOINT}/<change_id>", methods=["PATCH"])
# @user_required([EDIT_DISTRIBUTOR])
def patch_change(change_id):
    """
    PATCH endpoint to update a new Change.
    """
    change = ChangeController.update(id=change_id, **request.json)
    return jsonify(change_schema.dump(change))

@change_blueprint.route(f"{CHANGES_ENDPOINT}/<change_id>", methods=["DELETE"])
# @user_required([EDIT_DISTRIBUTOR])
def delete_change(change_id):
    """
    DELETE endpoint to delete a given Change.
    """
    change = ChangeController.load_by_id(change_id)
    try:
        ChangeController.delete(change)
    except Exception as e:
        return jsonify({"error": str(e)}), 404


@change_blueprint.route(f"{CHANGES_ENDPOINT}/all", methods=["DELETE"])
# @user_required([EDIT_DISTRIBUTOR])
def delete_all():
    """
    DELETE endpoint to delete all Changes.
    """
    changes_amount = ChangeController.count()
    ChangeController.delete_all()
    return f"{changes_amount} changes have been deleted"


@change_blueprint.route(f"{CHANGES_ENDPOINT}/<change_id>/apply", methods=["POST"])
def apply_change(change_id):
    """
    Applies change
    """
    try:
        ChangeController.apply_change(int(change_id))
        return "Cambio aplicado", 200
    except Exception as e:
        print(e)
        return ErrorHandler.determine_http_error_response(e)

@change_blueprint.route(f"{CHANGES_ENDPOINT}/<change_id>/discard", methods=["POST"])
def discard_change(change_id):
    """
    DiscardsChange
    """
    try:
        ChangeController.discard_change(int(change_id))
        return "Cambio rechazado", 200
    except Exception as e:
        return ErrorHandler.determine_http_error_response(e)


@change_blueprint.route(
    f"{CHANGES_ENDPOINT}/<change_id>/comments", methods=["POST"]
)
# @user_required([EDIT_DISTRIBUTOR])
def add_comment_to_change(change_id):
    """
    Add comment to an change
    """
    comment = request.json["comment"]
    created_by = request.json["created_by"]
    ChangeController.add_comment_to_solvable(
        solvable_id=change_id, comment_message=comment, created_by=created_by
    )
    return jsonify({"message": "Comment added"})
