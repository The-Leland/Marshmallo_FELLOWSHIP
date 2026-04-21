


from flask import Blueprint, request, jsonify
from controllers.hero_controller import (
    create_hero,
    get_all_heroes,
    get_hero_by_id,
    update_hero,
    delete_hero,
    get_alive_heroes
)
from models.hero import HeroSchema

hero_bp = Blueprint("hero_bp", __name__)


@hero_bp.route('/hero', methods=['POST'])
def add_hero():
    hero = create_hero(request.get_json())
    return jsonify(HeroSchema().dump(hero)), 201


@hero_bp.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = get_all_heroes()
    return jsonify(HeroSchema(many=True).dump(heroes)), 200


@hero_bp.route('/hero/<uuid:hero_id>', methods=['GET'])
def get_single_hero(hero_id):
    hero = get_hero_by_id(hero_id)
    if not hero:
        return {"message": "Hero not found"}, 404
    return jsonify(hero_schema.dump(hero)), 200


@hero_bp.route('/hero/<uuid:hero_id>', methods=['PUT'])
def update_hero_route(hero_id):
    updated = update_hero(hero_id, request.get_json())
    if not updated:
        return {"message": "Hero not found"}, 404
    return jsonify(hero_schema.dump(updated)), 200


@hero_bp.route('/hero/<uuid:hero_id>', methods=['DELETE'])
def delete_hero_route(hero_id):
    deleted = delete_hero(hero_id)

    if deleted == "blocked":
        return {"message": "Cannot delete hero: abilities or quests still linked"}, 400

    if deleted is None:
        return {"message": "Hero not found"}, 404

    return {"message": "Hero deleted successfully"}, 200


@hero_bp.route('/heroes/alive', methods=['GET'])
def get_alive_heroes_route():
    alive = get_alive_heroes()
    return jsonify(heroes_schema.dump(alive)), 200

