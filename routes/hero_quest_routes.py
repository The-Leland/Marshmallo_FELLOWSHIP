


from flask import Blueprint
from controllers.hero_quest_controller import (
    add_hero_quest,
    get_all_hero_quests,
    get_hero_quest,
    update_hero_quest,
    delete_hero_quest,
    get_quests_by_hero,
    get_heroes_by_quest
)

hero_quest_bp = Blueprint("hero_quest_bp", __name__)


@hero_quest_bp.route("/hero-quest", methods=["POST"])
def route_add_hero_quest():
    return add_hero_quest()


@hero_quest_bp.route("/hero-quests", methods=["GET"])
def route_get_all_hero_quests():
    return get_all_hero_quests()


@hero_quest_bp.route("/hero-quest/<uuid:hero_id>/<uuid:quest_id>", methods=["GET"])
def route_get_hero_quest(hero_id, quest_id):
    return get_hero_quest(hero_id, quest_id)


@hero_quest_bp.route("/hero-quest/<uuid:hero_id>/<uuid:quest_id>", methods=["PUT"])
def route_update_hero_quest(hero_id, quest_id):
    return update_hero_quest(hero_id, quest_id)


@hero_quest_bp.route("/hero-quest/<uuid:hero_id>/<uuid:quest_id>", methods=["DELETE"])
def route_delete_hero_quest(hero_id, quest_id):
    return delete_hero_quest(hero_id, quest_id)


@hero_quest_bp.route("/hero/<uuid:hero_id>/quests", methods=["GET"])
def route_get_quests_by_hero(hero_id):
    return get_quests_by_hero(hero_id)


@hero_quest_bp.route("/quest/<uuid:quest_id>/heroes", methods=["GET"])
def route_get_heroes_by_quest(quest_id):
    return get_heroes_by_quest(quest_id)

