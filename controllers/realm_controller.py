


from models.reflected import Realms, Locations
from schemas.realm_schema import RealmSchema
from sqlalchemy.orm import Session
from db import db

realm_schema = RealmSchema()
realms_schema = RealmSchema(many=True)

def get_all_realms():
    with Session(db.engine) as session:
        realms = session.query(Realms).all()
        return realms_schema.dump(realms)

def get_realm_by_id(realm_id):
    with Session(db.engine) as session:
        realm = session.get(Realms, realm_id)
        if not realm:
            return None
        return realm_schema.dump(realm)

def create_realm(data):
    with Session(db.engine) as session:
        realm = Realms(**data)
        session.add(realm)
        session.commit()
        return realm_schema.dump(realm)

def update_realm(realm_id, data):
    with Session(db.engine) as session:
        realm = session.get(Realms, realm_id)
        if not realm:
            return None
        for key, value in data.items():
            setattr(realm, key, value)
        session.commit()
        return realm_schema.dump(realm)

def delete_realm(realm_id):
    with Session(db.engine) as session:
        locations_exist = session.query(Locations).filter(Locations.realm_id == realm_id).first()
        if locations_exist:
            return "blocked"
        realm = session.get(Realms, realm_id)
        if not realm:
            return None
        session.delete(realm)
        session.commit()
        return True
    