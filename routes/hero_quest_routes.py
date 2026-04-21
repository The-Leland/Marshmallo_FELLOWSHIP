


from flask import Blueprint, request, jsonify
from controllers.hero_quest_controller import (
    create_hero_quest,
    get_all_hero_quests,
    get_hero_quest,
    update_hero_quest,
    delete_hero_quest,
    get_quests_by_hero,
    get_heroes_by_quest
)
from models.hero_quest import HeroQuestSchema

hero_quest_bp = Blueprint("hero_quest_bp", __name__)


@hero_quest_bp.route('/hero-quest', methods=['POST'])
def add_hero_quest():
    link = create_hero_quest(request.get_json())
    return jsonify(HeroQuestSchema.dump(link)), 201


@hero_quest_bp.route('/hero-quests', methods=['GET'])
def list_hero_quests():
    links = get_all_hero_quests()
    return jsonify(HeroQuestSchema.dump(links)), 200


@hero_quest_bp.route('/hero-quest/<uuid:hero_id>/<uuid:quest_id>', methods=['GET'])
def get_single_hero_quest(hero_id, quest_id):
    link = get_hero_quest(hero_id, quest_id)
    if not link:
        return {"message": "HeroQuest link not found"}, 404
    return jsonify(hero_quest_schema.dump(link)), 200


@hero_quest_bp.route('/hero/<uuid:hero_id>/quests', methods=['GET'])
def get_quests_for_hero(hero_id):
    quests = get_quests_by_hero(hero_id)
    return jsonify([q.quest_id for q in quests]), 200


@hero_quest_bp.route('/quest/<uuid:quest_id>/heroes', methods=['GET'])
def get_heroes_for_quest(quest_id):
    heroes = get_heroes_by_quest(quest_id)
    return jsonify([h.hero_id for h in heroes]), 200


@hero_quest_bp.route('/hero-quest/<uuid:hero_id>/<uuid:quest_id>', methods=['PUT'])
def update_hero_quest_route(hero_id, quest_id):
    updated = update_hero_quest(hero_id, quest_id, request.get_json())
    if not updated:
        return {"message": "HeroQuest link not found"}, 404
    return jsonify(hero_quest_schema.dump(updated)), 200


@hero_quest_bp.route('/hero-quest/<uuid:hero_id>/<uuid:quest_id>', methods=['DELETE'])
def delete_hero_quest_route(hero_id, quest_id):
    deleted = delete_hero_quest(hero_id, quest_id)

    if deleted is None:
        return {"message": "HeroQuest link not found"}, 404

    return {"message": "HeroQuest link deleted successfully"}, 200

