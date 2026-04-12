

from models.reflected import Locations, Quests
from schemas.location_schema import LocationSchema
from sqlalchemy.orm import Session
from db import db

location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)

def get_all_locations():
    with Session(db.engine) as session:
        locations = session.query(Locations).all()
        return locations_schema.dump(locations)

def get_location_by_id(location_id):
    with Session(db.engine) as session:
        location = session.get(Locations, location_id)
        if not location:
            return None
        return location_schema.dump(location)

def create_location(data):
    with Session(db.engine) as session:
        location = Locations(**data)
        session.add(location)
        session.commit()
        return location_schema.dump(location)

def update_location(location_id, data):
    with Session(db.engine) as session:
        location = session.get(Locations, location_id)
        if not location:
            return None
        for key, value in data.items():
            setattr(location, key, value)
        session.commit()
        return location_schema.dump(location)

def delete_location(location_id):
    with Session(db.engine) as session:
        quests_exist = session.query(Quests).filter(Quests.location_id == location_id).first()
        if quests_exist:
            return "blocked"
        location = session.get(Locations, location_id)
        if not location:
            return None
        session.delete(location)
        session.commit()
        return True