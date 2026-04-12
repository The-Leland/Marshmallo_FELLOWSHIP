


from flask import Blueprint, request, jsonify
from controllers.hero_quest_controller import (
    create_hero_quest,
    get_all_hero_quests,
    get_hero_quest,
    update_hero_quest,
    delete_hero_quest
)
from schemas.hero_quest_schema import HeroQuestSchema

hero_quest_bp = Blueprint("hero_quest_bp", __name__)
hero_quest_schema = HeroQuestSchema()
hero_quest_list_schema = HeroQuestSchema(many=True)


@hero_quest_bp.route('/hero-quest', methods=['POST'])
def add_hero_quest():
    link = create_hero_quest(request.get_json())
    if not link:
        return {"message": "Unable to assign hero to quest"}, 400
    return jsonify(hero_quest_schema.dump(link)), 201


@hero_quest_bp.route('/hero-quests', methods=['GET'])
def list_hero_quests():
    links = get_all_hero_quests()
    return jsonify(hero_quest_list_schema.dump(links)), 200


@hero_quest_bp.route('/hero-quest/<uuid:hero_quest_id>', methods=['GET'])
def get_single_hero_quest(hero_quest_id):
    link = get_hero_quest(hero_quest_id)
    if not link:
        return {"message": "HeroQuest link not found"}, 404
    return jsonify(hero_quest_schema.dump(link)), 200

@hero_quest_bp.route('/hero/<uuid:hero_id>/quests', methods=['GET'])
def get_quests_for_hero(hero_id):
    from controllers.hero_quest_controller import get_quests_by_hero
    quests = get_quests_by_hero(hero_id)
    return jsonify(quests), 200


@hero_quest_bp.route('/quest/<uuid:quest_id>/heroes', methods=['GET'])
def get_heroes_for_quest(quest_id):
    from controllers.hero_quest_controller import get_heroes_by_quest
    heroes = get_heroes_by_quest(quest_id)
    return jsonify(heroes), 200


@hero_quest_bp.route('/hero-quest/<uuid:hero_quest_id>', methods=['PUT'])
def update_hero_quest_route(hero_quest_id):
    updated = update_hero_quest(hero_quest_id, request.get_json())
    if not updated:
        return {"message": "Unable to update hero quest link"}, 400
    return jsonify(hero_quest_schema.dump(updated)), 200


@hero_quest_bp.route('/hero-quest/delete/<uuid:hero_quest_id>', methods=['DELETE'])
def delete_hero_quest_route(hero_quest_id):
    deleted = delete_hero_quest(hero_quest_id)

    if deleted is None:
        return {"message": "HeroQuest link not found"}, 404

    return jsonify(hero_quest_schema.dump(deleted)), 200
