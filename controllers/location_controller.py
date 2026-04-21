

from db import db
from models.location import Locations
from models.quest import Quests


def get_all_locations():
    return db.session.query(Locations).all()


def get_location_by_id(location_id):
    return db.session.query(Locations).filter_by(location_id=location_id).first()


def create_location(data):
    location = Locations(
        realm_id=data.get("realm_id"),
        location_name=data.get("location_name"),
        danger_level=data.get("danger_level")
    )
    db.session.add(location)
    db.session.commit()
    return location


def update_location(location_id, data):
    location = db.session.query(Locations).filter_by(location_id=location_id).first()
    if not location:
        return None

    for key, value in data.items():
        setattr(location, key, value)

    db.session.commit()
    return location


def delete_location(location_id):
    quest_exists = db.session.query(Quests).filter_by(location_id=location_id).first()
    if quest_exists:
        return "blocked"

    location = db.session.query(Locations).filter_by(location_id=location_id).first()
    if not location:
        return None

    db.session.delete(location)
    db.session.commit()
    return True
