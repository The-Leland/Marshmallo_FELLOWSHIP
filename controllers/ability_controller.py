


from flask import request, jsonify
from db import db
from models.ability import Abilities, ability_schema, abilities_schema
from models.hero import Heroes
from models.race import Races
from utils.reflection import populate_object




def add_ability():
    data = request.get_json()
    new_ability = Abilities(
        ability_name=data.get("ability_name"),
        hero_id=data.get("hero_id"),
        power_level=data.get("power_level")
    )

    db.session.add(new_ability)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to create ability"}), 400

    return jsonify(ability_schema.dump(new_ability)), 201


def get_all_abilities():
    abilities = db.session.query(Abilities).all()
    return jsonify(abilities_schema.dump(abilities)), 200


def get_ability_by_id(ability_id):
    ability = db.session.query(Abilities).filter(Abilities.ability_id == ability_id).first()

    if not ability:
        return jsonify({"message": "Ability not found"}), 404

    return jsonify(ability_schema.dump(ability)), 200


def update_ability(ability_id):
    ability = db.session.query(Abilities).filter(Abilities.ability_id == ability_id).first()

    if not ability:
        return jsonify({"message": "Ability not found"}), 404

    data = request.get_json()
    populate_object(ability, data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to update ability"}), 400

    return jsonify(ability_schema.dump(ability)), 200


def delete_ability(ability_id):
    ability = db.session.query(Abilities).filter(Abilities.ability_id == ability_id).first()

    if not ability:
        return jsonify({"message": "Ability not found"}), 404

    db.session.delete(ability)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to delete ability"}), 400

    return jsonify({"message": "Ability deleted successfully"}), 200


