


from db import db
from models.realm import Realms
from models.location import Locations


def get_all_realms():
    return db.session.query(Realms).all()


def get_realm_by_id(realm_id):
    return db.session.query(Realms).filter_by(realm_id=realm_id).first()


def create_realm(data):
    realm = Realms(
        realm_name=data.get("realm_name"),
        ruler=data.get("ruler")
    )
    db.session.add(realm)
    db.session.commit()
    return realm


def update_realm(realm_id, data):
    realm = db.session.query(Realms).filter_by(realm_id=realm_id).first()
    if not realm:
        return None

    for key, value in data.items():
        setattr(realm, key, value)

    db.session.commit()
    return realm


def delete_realm(realm_id):
    location_exists = db.session.query(Locations).filter_by(realm_id=realm_id).first()
    if location_exists:
        return "blocked"

    realm = db.session.query(Realms).filter_by(realm_id=realm_id).first()
    if not realm:
        return None

    db.session.delete(realm)
    db.session.commit()
    return True
