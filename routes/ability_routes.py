from flask import Blueprint, request, jsonify
from controllers.ability_controller import (
    create_ability,
    get_all_abilities,
    get_ability_by_id,
    update_ability,
    delete_ability
)
from schemas.ability_schema import AbilitySchema

ability_bp = Blueprint("ability_bp", __name__)
ability_schema = AbilitySchema()
ability_list_schema = AbilitySchema(many=True)


@ability_bp.route('/ability', methods=['POST'])
def add_ability():
    ability = create_ability(request.get_json())
    if not ability:
        return {"message": "Unable to create ability"}, 400
    return jsonify(ability_schema.dump(ability)), 201


@ability_bp.route('/abilities', methods=['GET'])
def list_abilities():
    abilities = get_all_abilities()
    return jsonify(ability_list_schema.dump(abilities)), 200


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
        return {"message": "Unable to update ability"}, 400
    return jsonify(ability_schema.dump(updated)), 200


@ability_bp.route('/ability/delete/<uuid:ability_id>', methods=['DELETE'])
def delete_ability_route(ability_id):
    deleted = delete_ability(ability_id)

    if deleted is False:
        return {"message": "Cannot delete ability while hero still has it"}, 400

    if deleted is None:
        return {"message": "Ability not found"}, 404

    return jsonify(ability_schema.dump(deleted)), 200
