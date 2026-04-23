


from flask import Blueprint
from controllers.location_controller import (
    add_location,
    get_all_locations,
    get_location_by_id,
    update_location,
    delete_location
)

location_bp = Blueprint("location_bp", __name__)


@location_bp.route("/location", methods=["POST"])
def route_add_location():
    return add_location()


@location_bp.route("/locations", methods=["GET"])
def route_get_all_locations():
    return get_all_locations()


@location_bp.route("/location/<uuid:location_id>", methods=["GET"])
def route_get_location_by_id(location_id):
    return get_location_by_id(location_id)


@location_bp.route("/location/<uuid:location_id>", methods=["PUT"])
def route_update_location(location_id):
    return update_location(location_id)


@location_bp.route("/location/<uuid:location_id>", methods=["DELETE"])
def route_delete_location(location_id):
    return delete_location(location_id)

