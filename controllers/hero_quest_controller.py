


from flask import request, jsonify
from db import db
from models.hero_quest import HeroQuest, hero_quest_schema, hero_quests_schema
from models.hero import Heroes, heroes_schema
from models.quest import Quests, quests_schema
from utils.reflection import populate_object


def add_hero_quest():
    data = request.get_json()
    new_record = HeroQuest(
        hero_id=data.get("hero_id"),
        quest_id=data.get("quest_id"),
        date_joined=data.get("date_joined")
    )

    db.session.add(new_record)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to create hero_quest record"}), 400

    return jsonify(hero_quest_schema().dump(new_record)), 201


def get_all_hero_quests():
    records = db.session.query(HeroQuest).all()
    return jsonify(hero_quests_schema().dump(records)), 200


def get_hero_quest(hero_id, quest_id):
    record = (
        db.session.query(HeroQuest)
        .filter(HeroQuest.hero_id == hero_id, HeroQuest.quest_id == quest_id)
        .first()
    )

    if not record:
        return jsonify({"message": "HeroQuest record not found"}), 404

    return jsonify(hero_quest_schema().dump(record)), 200


def update_hero_quest(hero_id, quest_id):
    record = (
        db.session.query(HeroQuest)
        .filter(HeroQuest.hero_id == hero_id, HeroQuest.quest_id == quest_id)
        .first()
    )

    if not record:
        return jsonify({"message": "HeroQuest record not found"}), 404

    data = request.get_json()
    populate_object(record, data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to update hero_quest record"}), 400

    return jsonify(hero_quest_schema().dump(record)), 200


def delete_hero_quest(hero_id, quest_id):
    record = (
        db.session.query(HeroQuest)
        .filter(HeroQuest.hero_id == hero_id, HeroQuest.quest_id == quest_id)
        .first()
    )

    if not record:
        return jsonify({"message": "HeroQuest record not found"}), 404

    db.session.delete(record)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to delete hero_quest record"}), 400

    return jsonify({"message": "HeroQuest record deleted successfully"}), 200


def get_quests_by_hero(hero_id):
    quests = (
        db.session.query(Quests)
        .join(HeroQuest, HeroQuest.quest_id == Quests.quest_id)
        .filter(HeroQuest.hero_id == hero_id)
        .all()
    )

    return jsonify(quests_schema().dump(quests)), 200


def get_heroes_by_quest(quest_id):
    heroes = (
        db.session.query(Heroes)
        .join(HeroQuest, HeroQuest.hero_id == Heroes.hero_id)
        .filter(HeroQuest.quest_id == quest_id)
        .all()
    )

    return jsonify(heroes_schema().dump(heroes)), 200

