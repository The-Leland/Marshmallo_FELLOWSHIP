

from flask import request, jsonify
from db import db
from models.race import Races, race_schema, races_schema
from utils.reflection import populate_object




def add_race():
    data = request.get_json()
    new_race = Races(
        race_name=data.get("race_name"),
        homeland=data.get("homeland"),
        lifespan=data.get("lifespan")
    )

    db.session.add(new_race)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to create race"}), 400

    return jsonify(race_schema.dump(new_race)), 201


def get_all_races():
    races = db.session.query(Races).all()
    return jsonify(races_schema.dump(races)), 200


def get_race_by_id(race_id):
    race = db.session.query(Races).filter(Races.race_id == race_id).first()

    if not race:
        return jsonify({"message": "Race not found"}), 404

    return jsonify(race_schema.dump(race)), 200


def update_race(race_id):
    race = db.session.query(Races).filter(Races.race_id == race_id).first()

    if not race:
        return jsonify({"message": "Race not found"}), 404

    data = request.get_json()
    populate_object(race, data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to update race"}), 400

    return jsonify(race_schema.dump(race)), 200


def delete_race(race_id):
    race = db.session.query(Races).filter(Races.race_id == race_id).first()

    if not race:
        return jsonify({"message": "Race not found"}), 404

    if race.heroes:
        return jsonify({"message": "Cannot delete race: heroes still linked"}), 400

    db.session.delete(race)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to delete race"}), 400

    return jsonify({"message": "Race deleted successfully"}), 200

