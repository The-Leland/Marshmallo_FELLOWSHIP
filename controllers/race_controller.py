


from flask import request, jsonify
from sqlalchemy.orm import joinedload
from db import db
from models.race import Races, race_schema, races_schema
from utils.reflection import populate_object

def add_race():
    post_data = request.form if request.form else request.get_json()

    lifespan = post_data.get("lifespan")
    if lifespan is not None:
        try:
            lifespan = int(lifespan)
        except ValueError:
            return jsonify({"message": "lifespan must be an integer"}), 400

    new_race = Races(
        race_name=post_data.get("race_name"),
        homeland=post_data.get("homeland"),
        lifespan=lifespan
    )

    db.session.add(new_race)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        print(" ERROR CREATING RACE:", e)
        return jsonify({"message": "Unable to create race"}), 400

    schema = race_schema()
    return jsonify({"message": "race created", "results": schema.dump(new_race)}), 201

def get_all_races():
    races = db.session.query(Races).options(joinedload(Races.heroes)).all()
    schema = races_schema()
    return jsonify({"message": "races retrieved", "results": schema.dump(races)}), 200


def get_race_by_id(race_id):
    race = db.session.query(Races).options(joinedload(Races.heroes)).filter(Races.race_id == race_id).first()

    if not race:
        return jsonify({"message": "Race not found"}), 404

    schema = race_schema()
    return jsonify({"message": "race found", "results": schema.dump(race)}), 200


def update_race(race_id):
    race = db.session.query(Races).filter(Races.race_id == race_id).first()

    if not race:
        return jsonify({"message": "Race not found"}), 404

    post_data = request.form if request.form else request.get_json()
    populate_object(race, post_data)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to update race"}), 400

    schema = race_schema()
    return jsonify({"message": "race updated", "results": schema.dump(race)}), 200


def delete_race(race_id):
    race = db.session.query(Races).filter(Races.race_id == race_id).first()

    if not race:
        return jsonify({"message": "Race not found"}), 404

    if hasattr(race, "heroes") and race.heroes:
        return jsonify({"message": "Cannot delete race: heroes still linked"}), 400

    db.session.delete(race)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to delete race"}), 400

    return jsonify({"message": "Race deleted successfully"}), 200
