


from flask import request, jsonify
from db import db
from models.hero import Heroes, hero_schema, heroes_schema
from utils.reflection import populate_object


def add_hero():
    data = request.get_json()
    new_hero = Heroes(
        hero_name=data.get("hero_name"),
        race_id=data.get("race_id"),
        age=data.get("age"),
        health_points=data.get("health_points"),
        is_alive=data.get("is_alive", True)
    )

    db.session.add(new_hero)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to create hero"}), 400

    return jsonify(hero_schema().dump(new_hero)), 201


def get_all_heroes():
    heroes = db.session.query(Heroes).all()
    return jsonify(heroes_schema().dump(heroes)), 200


def get_hero_by_id(hero_id):
    hero = db.session.query(Heroes).filter(Heroes.hero_id == hero_id).first()

    if not hero:
        return jsonify({"message": "Hero not found"}), 404

    return jsonify(hero_schema().dump(hero)), 200


def get_alive_heroes():
    alive = db.session.query(Heroes).filter(Heroes.is_alive == True).all()
    return jsonify(heroes_schema().dump(alive)), 200


def update_hero(hero_id):
    hero = db.session.query(Heroes).filter(Heroes.hero_id == hero_id).first()

    if not hero:
        return jsonify({"message": "Hero not found"}), 404

    data = request.get_json()
    populate_object(hero, data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to update hero"}), 400

    return jsonify(hero_schema().dump(hero)), 200


def delete_hero(hero_id):
    hero = db.session.query(Heroes).filter(Heroes.hero_id == hero_id).first()

    if not hero:
        return jsonify({"message": "Hero not found"}), 404

    if hero.abilities or hero.quests:
        return jsonify({"message": "Cannot delete hero: abilities or quests still linked"}), 400

    db.session.delete(hero)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to delete hero"}), 400

    return jsonify({"message": "Hero deleted successfully"}), 200
