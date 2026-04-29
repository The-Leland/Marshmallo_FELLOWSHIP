


from flask import request, jsonify
from sqlalchemy.orm import joinedload
from db import db
from models.hero_quest import HeroQuests, hero_quest_schema, hero_quests_schema
from models.hero import Heroes, heroes_schema
from models.quest import Quests, quests_schema
from utils.reflection import populate_object

def add_hero_quest():
    post_data = request.form if request.form else request.get_json()

    new_record = HeroQuests(
        hero_id=post_data.get("hero_id"),
        quest_id=post_data.get("quest_id"),
        date_joined=post_data.get("date_joined")
    )

    db.session.add(new_record)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to create hero_quest record"}), 400

    schema = hero_quest_schema()
    return jsonify({"message": "hero_quest created", "results": schema.dump(new_record)}), 201


def get_all_hero_quests():
    records = db.session.query(HeroQuests).all()
    schema = hero_quests_schema()
    return jsonify({"message": "hero_quests retrieved", "results": schema.dump(records)}), 200


def get_hero_quest(hero_id, quest_id):
    record = (
        db.session.query(HeroQuests)
        .filter(HeroQuests.hero_id == hero_id, HeroQuests.quest_id == quest_id)
        .first()
    )

    if not record:
        return jsonify({"message": "HeroQuest record not found"}), 404

    schema = hero_quest_schema()
    return jsonify({"message": "hero_quest found", "results": schema.dump(record)}), 200


def update_hero_quest(hero_id, quest_id):
    record = (
        db.session.query(HeroQuests)
        .filter(HeroQuests.hero_id == hero_id, HeroQuests.quest_id == quest_id)
        .first()
    )

    if not record:
        return jsonify({"message": "HeroQuest record not found"}), 404

    post_data = request.form if request.form else request.get_json()
    populate_object(record, post_data)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to update hero_quest record"}), 400

    schema = hero_quest_schema()
    return jsonify({"message": "hero_quest updated", "results": schema.dump(record)}), 200


def delete_hero_quest(hero_id, quest_id):
    record = (
        db.session.query(HeroQuests)
        .filter(HeroQuests.hero_id == hero_id, HeroQuests.quest_id == quest_id)
        .first()
    )

    if not record:
        return jsonify({"message": "HeroQuest record not found"}), 404

    db.session.delete(record)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to delete hero_quest record"}), 400

    return jsonify({"message": "HeroQuest record deleted successfully"}), 200


def get_quests_by_hero(hero_id):
    quests = (
        db.session.query(Quests)
        .join(HeroQuests, HeroQuests.quest_id == Quests.quest_id)
        .filter(HeroQuests.hero_id == hero_id)
        .options(joinedload(Quests.location))
        .all()
    )

    schema = quests_schema()
    return jsonify({"message": "quests for hero retrieved", "results": schema.dump(quests)}), 200


def get_heroes_by_quest(quest_id):
    heroes = (
        db.session.query(Heroes)
        .join(HeroQuests, HeroQuests.hero_id == Heroes.hero_id)
        .filter(HeroQuests.quest_id == quest_id)
        .options(joinedload(Heroes.abilities))
        .all()
    )

    schema = heroes_schema()
    return jsonify({"message": "heroes for quest retrieved", "results": schema.dump(heroes)}), 200
