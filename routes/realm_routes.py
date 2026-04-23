



from flask import Blueprint
from controllers.realm_controller import (
    add_realm,
    get_all_realms,
    get_realm_by_id,
    update_realm,
    delete_realm
)

realm_bp = Blueprint("realm_bp", __name__)


@realm_bp.route("/realm", methods=["POST"])
def route_add_realm():
    return add_realm()


@realm_bp.route("/realms", methods=["GET"])
def route_get_all_realms():
    return get_all_realms()


@realm_bp.route("/realm/<uuid:realm_id>", methods=["GET"])
def route_get_realm_by_id(realm_id):
    return get_realm_by_id(realm_id)


@realm_bp.route("/realm/<uuid:realm_id>", methods=["PUT"])
def route_update_realm(realm_id):
    return update_realm(realm_id)


@realm_bp.route("/realm/<uuid:realm_id>", methods=["DELETE"])
def route_delete_realm(realm_id):
    return delete_realm(realm_id)
