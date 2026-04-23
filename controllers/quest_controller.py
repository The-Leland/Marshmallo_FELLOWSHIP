


from flask import request, jsonify
from db import db
from models.quest import Quests, quest_schema, quests_schema
from utils.reflection import populate_object




def add_quest():
    data = request.get_json()
    new_quest = Quests(
        quest_name=data.get("quest_name"),
        location_id=data.get("location_id"),
        difficulty=data.get("difficulty"),
        reward_gold=data.get("reward_gold"),
        is_completed=data.get("is_completed", False)
    )

    db.session.add(new_quest)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to create quest"}), 400

    return jsonify(quest_schema.dump(new_quest)), 201


def get_all_quests():
    quests = db.session.query(Quests).all()
    return jsonify(quests_schema.dump(quests)), 200


def get_quests_by_difficulty(level):
    quests = db.session.query(Quests).filter(Quests.difficulty == level).all()
    return jsonify(quests_schema.dump(quests)), 200


def get_quest_by_id(quest_id):
    quest = db.session.query(Quests).filter(Quests.quest_id == quest_id).first()

    if not quest:
        return jsonify({"message": "Quest not found"}), 404

    return jsonify(quest_schema.dump(quest)), 200


def update_quest(quest_id):
    quest = db.session.query(Quests).filter(Quests.quest_id == quest_id).first()

    if not quest:
        return jsonify({"message": "Quest not found"}), 404

    data = request.get_json()
    populate_object(quest, data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to update quest"}), 400

    return jsonify(quest_schema.dump(quest)), 200


def complete_quest(quest_id):
    quest = db.session.query(Quests).filter(Quests.quest_id == quest_id).first()

    if not quest:
        return jsonify({"message": "Quest not found"}), 404

    quest.is_completed = True

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to complete quest"}), 400

    return jsonify(quest_schema.dump(quest)), 200


def delete_quest(quest_id):
    quest = db.session.query(Quests).filter(Quests.quest_id == quest_id).first()

    if not quest:
        return jsonify({"message": "Quest not found"}), 404

    db.session.delete(quest)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to delete quest"}), 400

    return jsonify({"message": "Quest deleted successfully"}), 200


