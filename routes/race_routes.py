





from flask import Blueprint, request, jsonify
from controllers.race_controller import (
    create_race,
    get_all_races,
    get_race_by_id,
    update_race,
    delete_race
)
from schemas.race_schema import RaceSchema

race_bp = Blueprint("race_bp", __name__)
race_schema = RaceSchema()
race_list_schema = RaceSchema(many=True)


@race_bp.route('/race', methods=['POST'])
def add_race():
    race = create_race(request.get_json())
    if not race:
        return {"message": "Unable to create race"}, 400
    return jsonify(race_schema.dump(race)), 201


@race_bp.route('/races', methods=['GET'])
def list_races():
    races = get_all_races()
    return jsonify(race_list_schema.dump(races)), 200


@race_bp.route('/race/<uuid:race_id>', methods=['GET'])
def get_single_race(race_id):
    race = get_race_by_id(race_id)
    if not race:
        return {"message": "Race not found"}, 404
    return jsonify(race_schema.dump(race)), 200


@race_bp.route('/race/<uuid:race_id>', methods=['PUT'])
def update_race_route(race_id):
    updated = update_race(race_id, request.get_json())
    if not updated:
        return {"message": "Unable to update race"}, 400
    return jsonify(race_schema.dump(updated)), 200


@race_bp.route('/race/delete/<uuid:race_id>', methods=['DELETE'])
def delete_race_route(race_id):
    deleted = delete_race(race_id)

    if deleted is False:
        return {"message": "Cannot delete race: heroes still belong to this race"}, 400

    if deleted is None:
        return {"message": "Race not found"}, 404

    return jsonify(race_schema.dump(deleted)), 200

