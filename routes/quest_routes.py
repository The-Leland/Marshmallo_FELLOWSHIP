


from flask import Blueprint
from controllers.quest_controller import (
    add_quest,
    get_all_quests,
    get_quests_by_difficulty,
    get_quest_by_id,
    update_quest,
    complete_quest,
    delete_quest
)

quest_bp = Blueprint("quest_bp", __name__)


@quest_bp.route("/quest", methods=["POST"])
def route_add_quest():
    return add_quest()


@quest_bp.route("/quests", methods=["GET"])
def route_get_all_quests():
    return get_all_quests()


@quest_bp.route("/quests/<difficulty>", methods=["GET"])
def route_get_quests_by_difficulty(difficulty):
    return get_quests_by_difficulty(difficulty)


@quest_bp.route("/quest/<uuid:quest_id>", methods=["GET"])
def route_get_quest_by_id(quest_id):
    return get_quest_by_id(quest_id)


@quest_bp.route("/quest/<uuid:quest_id>", methods=["PUT"])
def route_update_quest(quest_id):
    return update_quest(quest_id)


@quest_bp.route("/quest/<uuid:quest_id>/complete", methods=["PUT"])
def route_complete_quest(quest_id):
    return complete_quest(quest_id)


@quest_bp.route("/quest/<uuid:quest_id>", methods=["DELETE"])
def route_delete_quest(quest_id):
    return delete_quest(quest_id)
