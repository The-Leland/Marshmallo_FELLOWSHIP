


from flask import request, jsonify
from sqlalchemy.orm import joinedload
from db import db
from models.quest import Quests, quest_schema, quests_schema
from models.hero_quest import HeroQuests
from utils.reflection import populate_object

def add_quest():
    post_data = request.form if request.form else request.get_json()

    new_quest = Quests(
        quest_name=post_data.get("quest_name"),
        location_id=post_data.get("location_id"),
        difficulty=post_data.get("difficulty"),
        reward_gold=post_data.get("reward_gold"),
        is_completed=post_data.get("is_completed", False)
    )

    db.session.add(new_quest)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to create quest"}), 400

    schema = quest_schema()
    return jsonify({"message": "quest created", "results": schema.dump(new_quest)}), 201


def get_all_quests():
    quests = db.session.query(Quests).options(joinedload(Quests.location)).all()
    schema = quests_schema()
    return jsonify({"message": "quests retrieved", "results": schema.dump(quests)}), 200


def get_quests_by_difficulty(level):
    quests = db.session.query(Quests).filter(Quests.difficulty == level).all()
    schema = quests_schema()
    return jsonify({"message": f"quests with difficulty {level} retrieved", "results": schema.dump(quests)}), 200


def get_quest_by_id(quest_id):
    quest = db.session.query(Quests).options(joinedload(Quests.location)).filter(Quests.quest_id == quest_id).first()

    if not quest:
        return jsonify({"message": "Quest not found"}), 404

    schema = quest_schema()
    return jsonify({"message": "quest found", "results": schema.dump(quest)}), 200


def update_quest(quest_id):
    quest = db.session.query(Quests).filter(Quests.quest_id == quest_id).first()

    if not quest:
        return jsonify({"message": "Quest not found"}), 404

    post_data = request.form if request.form else request.get_json()
    populate_object(quest, post_data)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to update quest"}), 400

    schema = quest_schema()
    return jsonify({"message": "quest updated", "results": schema.dump(quest)}), 200


def complete_quest(quest_id):
    quest = db.session.query(Quests).filter(Quests.quest_id == quest_id).first()

    if not quest:
        return jsonify({"message": "Quest not found"}), 404

    quest.is_completed = True

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to complete quest"}), 400

    schema = quest_schema()
    return jsonify({"message": "quest completed", "results": schema.dump(quest)}), 200


def delete_quest(quest_id):
    linked = db.session.query(HeroQuests).filter(HeroQuests.quest_id == quest_id).first()
    if linked:
        return jsonify({"message": "Cannot delete quest: heroes still linked"}), 400

    quest = db.session.query(Quests).filter(Quests.quest_id == quest_id).first()

    if not quest:
        return jsonify({"message": "Quest not found"}), 404

    db.session.delete(quest)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to delete quest"}), 400

    return jsonify({"message": "Quest deleted successfully"}), 200
