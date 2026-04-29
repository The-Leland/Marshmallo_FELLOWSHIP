


from flask import request, jsonify
from sqlalchemy.orm import joinedload
from db import db
from models.hero import Heroes, hero_schema, heroes_schema
from utils.reflection import populate_object

def add_hero():
    post_data = request.form if request.form else request.get_json()

    new_hero = Heroes(
        hero_name=post_data.get("hero_name"),
        race_id=post_data.get("race_id"),
        age=post_data.get("age"),
        health_points=post_data.get("health_points"),
        is_alive=post_data.get("is_alive", True)
    )

    db.session.add(new_hero)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to create hero"}), 400

    schema = hero_schema()
    return jsonify({"message": "hero created", "results": schema.dump(new_hero)}), 201


def get_all_heroes():
    heroes = db.session.query(Heroes).options(joinedload(Heroes.abilities)).all()
    schema = heroes_schema()
    return jsonify({"message": "heroes retrieved", "results": schema.dump(heroes)}), 200


def get_hero_by_id(hero_id):
    hero = db.session.query(Heroes).options(joinedload(Heroes.abilities)).filter(Heroes.hero_id == hero_id).first()

    if not hero:
        return jsonify({"message": "Hero not found"}), 404

    schema = hero_schema()
    return jsonify({"message": "hero found", "results": schema.dump(hero)}), 200


def get_alive_heroes():
    alive = db.session.query(Heroes).filter(Heroes.is_alive == True).all()
    schema = heroes_schema()
    return jsonify({"message": "alive heroes retrieved", "results": schema.dump(alive)}), 200


def update_hero(hero_id):
    hero = db.session.query(Heroes).filter(Heroes.hero_id == hero_id).first()

    if not hero:
        return jsonify({"message": "Hero not found"}), 404

    post_data = request.form if request.form else request.get_json()
    populate_object(hero, post_data)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to update hero"}), 400

    schema = hero_schema()
    return jsonify({"message": "hero updated", "results": schema.dump(hero)}), 200


def delete_hero(hero_id):
    hero = db.session.query(Heroes).filter(Heroes.hero_id == hero_id).first()

    if not hero:
        return jsonify({"message": "Hero not found"}), 404

    
    if (hasattr(hero, "abilities") and hero.abilities) or (hasattr(hero, "hero_quests") and hero.hero_quests):
        return jsonify({"message": "Cannot delete hero: abilities or quests still linked"}), 400

    db.session.delete(hero)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to delete hero"}), 400

    return jsonify({"message": "Hero deleted successfully"}), 200
