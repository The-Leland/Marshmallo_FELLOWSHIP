


from flask import Blueprint, request, jsonify
from controllers.quest_controller import (
    create_quest,
    get_all_quests,
    get_quest_by_id,
    update_quest,
    delete_quest
)
from models.quest import QuestSchema

quest_bp = Blueprint("quest_bp", __name__)


@quest_bp.route('/quest', methods=['POST'])
def add_quest():
    quest = create_quest(request.get_json())
    return jsonify(QuestSchema().dump(quest)), 201


@quest_bp.route('/quests', methods=['GET'])
def list_quests():
    quests = get_all_quests()
    return jsonify(quests_schema.dump(quests)), 200


@quest_bp.route('/quest/<uuid:quest_id>', methods=['GET'])
def get_single_quest(quest_id):
    quest = get_quest_by_id(quest_id)
    if not quest:
        return {"message": "Quest not found"}, 404
    return jsonify(quest_schema.dump(quest)), 200


@quest_bp.route('/quest/<uuid:quest_id>', methods=['PUT'])
def update_quest_route(quest_id):
    updated = update_quest(quest_id, request.get_json())
    if not updated:
        return {"message": "Quest not found"}, 404
    return jsonify(quest_schema.dump(updated)), 200


@quest_bp.route('/quest/<uuid:quest_id>', methods=['DELETE'])
def delete_quest_route(quest_id):
    deleted = delete_quest(quest_id)

    if deleted is None:
        return {"message": "Quest not found"}, 404

    return {"message": "Quest deleted successfully"}, 200

