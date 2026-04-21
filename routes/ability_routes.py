
from flask import Blueprint, request, jsonify
from controllers.ability_controller import (
    create_ability,
    get_all_abilities,
    get_ability_by_id,
    update_ability,
    delete_ability
)
from models.ability import AbilitySchema

ability_bp = Blueprint("ability_bp", __name__)


@ability_bp.route('/ability', methods=['POST'])
def add_ability():
    ability = create_ability(request.get_json())
    return jsonify(ability_schema.dump(ability)), 201


@ability_bp.route('/abilities', methods=['GET'])
def list_abilities():
    abilities = get_all_abilities()
    return jsonify(ability_schema.dump(abilities)), 200


@ability_bp.route('/ability/<uuid:ability_id>', methods=['GET'])
def get_single_ability(ability_id):
    ability = get_ability_by_id(ability_id)
    if not ability:
        return {"message": "Ability not found"}, 404
    return jsonify(ability_schema.dump(ability)), 200


@ability_bp.route('/ability/<uuid:ability_id>', methods=['PUT'])
def update_ability_route(ability_id):
    updated = update_ability(ability_id, request.get_json())
    if not updated:
        return {"message": "Ability not found"}, 404
    return jsonify(ability_schema.dump(updated)), 200


@ability_bp.route('/ability/<uuid:ability_id>', methods=['DELETE'])
def delete_ability_route(ability_id):
    deleted = delete_ability(ability_id)

    if deleted is None:
        return {"message": "Ability not found"}, 404

    return {"message": "Ability deleted successfully"}, 200
