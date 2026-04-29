


from flask import request, jsonify
from sqlalchemy.orm import joinedload
from db import db
from models.realm import Realms, realm_schema, realms_schema
from models.location import Locations
from utils.reflection import populate_object

def add_realm():
    post_data = request.form if request.form else request.get_json()

    new_realm = Realms(
        realm_name=post_data.get("realm_name"),
        ruler=post_data.get("ruler")
    )

    db.session.add(new_realm)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to create realm"}), 400

    schema = realm_schema()
    return jsonify({"message": "realm created", "results": schema.dump(new_realm)}), 201


def get_all_realms():
    realms = db.session.query(Realms).options(joinedload(Realms.locations)).all()
    schema = realms_schema()
    return jsonify({"message": "realms retrieved", "results": schema.dump(realms)}), 200


def get_realm_by_id(realm_id):
    realm = db.session.query(Realms).options(joinedload(Realms.locations)).filter(Realms.realm_id == realm_id).first()

    if not realm:
        return jsonify({"message": "Realm not found"}), 404

    schema = realm_schema()
    return jsonify({"message": "realm found", "results": schema.dump(realm)}), 200


def update_realm(realm_id):
    realm = db.session.query(Realms).filter(Realms.realm_id == realm_id).first()

    if not realm:
        return jsonify({"message": "Realm not found"}), 404

    post_data = request.form if request.form else request.get_json()
    populate_object(realm, post_data)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to update realm"}), 400

    schema = realm_schema()
    return jsonify({"message": "realm updated", "results": schema.dump(realm)}), 200


def delete_realm(realm_id):
    linked_location = db.session.query(Locations).filter(Locations.realm_id == realm_id).first()
    if linked_location:
        return jsonify({"message": "Cannot delete realm: locations still linked"}), 400

    realm = db.session.query(Realms).filter(Realms.realm_id == realm_id).first()
    if not realm:
        return jsonify({"message": "Realm not found"}), 404

    db.session.delete(realm)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Unable to delete realm"}), 400

    return jsonify({"message": "Realm deleted successfully"}), 200
