


from flask import Blueprint, request, jsonify
from controllers.location_controller import (
    create_location,
    get_all_locations,
    get_location_by_id,
    update_location,
    delete_location
)
from models.location import LocationSchema

location_bp = Blueprint("location_bp", __name__)


@location_bp.route('/location', methods=['POST'])
def add_location():
    location = create_location(request.get_json())
    return jsonify(LocationSchema().dump(location)), 201


@location_bp.route('/locations', methods=['GET'])
def list_locations():
    locations = get_all_locations()
    return jsonify(LocationSchema(many=True).dump(locations)), 200


@location_bp.route('/location/<uuid:location_id>', methods=['GET'])
def get_single_location(location_id):
    location = get_location_by_id(location_id)
    if not location:
        return {"message": "Location not found"}, 404
    return jsonify(location_schema.dump(location)), 200


@location_bp.route('/location/<uuid:location_id>', methods=['PUT'])
def update_location_route(location_id):
    updated = update_location(location_id, request.get_json())
    if not updated:
        return {"message": "Location not found"}, 404
    return jsonify(location_schema.dump(updated)), 200


@location_bp.route('/location/<uuid:location_id>', methods=['DELETE'])
def delete_location_route(location_id):
    deleted = delete_location(location_id)

    if deleted == "blocked":
        return {"message": "Cannot delete location: quests still belong to this location"}, 400

    if deleted is None:
        return {"message": "Location not found"}, 404

    return {"message": "Location deleted successfully"}, 200
