


from flask import request, jsonify
from sqlalchemy.orm import joinedload
from db import db
from models.location import Locations, location_schema, locations_schema
from models.quest import Quests, quests_schema
from utils.reflection import populate_object

def add_location():
    post_data = request.form if request.form else request.get_json()

    new_location = Locations(
        location_name=post_data.get("location_name"),
        realm_id=post_data.get("realm_id"),
        danger_level=post_data.get("danger_level")
    )

    db.session.add(new_location)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to create location"}), 400

    schema = location_schema()
    return jsonify({"message": "location created", "results": schema.dump(new_location)}), 201


def get_all_locations():
    
    locations = db.session.query(Locations).options(joinedload(Locations.quests)).all()
    schema = locations_schema()
    return jsonify({"message": "locations retrieved", "results": schema.dump(locations)}), 200


def get_location_by_id(location_id):
    location = db.session.query(Locations).options(joinedload(Locations.quests)).filter(Locations.location_id == location_id).first()

    if not location:
        return jsonify({"message": "Location not found"}), 404

    schema = location_schema()
    return jsonify({"message": "location found", "results": schema.dump(location)}), 200


def update_location(location_id):
    location = db.session.query(Locations).filter(Locations.location_id == location_id).first()

    if not location:
        return jsonify({"message": "Location not found"}), 404

    post_data = request.form if request.form else request.get_json()
    populate_object(location, post_data)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to update location"}), 400

    schema = location_schema()
    return jsonify({"message": "location updated", "results": schema.dump(location)}), 200


def delete_location(location_id):
    
    linked_quest = db.session.query(Quests).filter(Quests.location_id == location_id).first()
    if linked_quest:
        return jsonify({"message": "Cannot delete location: quests still linked"}), 400

    location = db.session.query(Locations).filter(Locations.location_id == location_id).first()
    if not location:
        return jsonify({"message": "Location not found"}), 404

    db.session.delete(location)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to delete location"}), 400

    return jsonify({"message": "Location deleted successfully"}), 200
