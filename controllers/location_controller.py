

from flask import request, jsonify
from db import db
from models.location import Locations
from models.quest import Quests
from models.location import Locations, location_schema, locations_schema
from utils.reflection import populate_object



def add_location():
    data = request.get_json()
    new_location = Locations(
        location_name=data.get("location_name"),
        realm_id=data.get("realm_id"),
        danger_level=data.get("danger_level")
    )

    db.session.add(new_location)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to create location"}), 400

    return jsonify(location_schema.dump(new_location)), 201


def get_all_locations():
    locations = db.session.query(Locations).all()
    return jsonify(locations_schema.dump(locations)), 200


def get_location_by_id(location_id):
    location = db.session.query(Locations).filter(Locations.location_id == location_id).first()

    if not location:
        return jsonify({"message": "Location not found"}), 404

    return jsonify(location_schema.dump(location)), 200


def update_location(location_id):
    location = db.session.query(Locations).filter(Locations.location_id == location_id).first()

    if not location:
        return jsonify({"message": "Location not found"}), 404

    data = request.get_json()
    populate_object(location, data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to update location"}), 400

    return jsonify(location_schema.dump(location)), 200


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
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to delete location"}), 400

    return jsonify({"message": "Location deleted successfully"}), 200
