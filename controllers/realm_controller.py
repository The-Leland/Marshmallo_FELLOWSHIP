


from flask import request, jsonify
from db import db
from models.realm import Realms, realm_schema, realms_schema
from models.location import Locations
from utils.reflection import populate_object




def add_realm():
    data = request.get_json()
    new_realm = Realms(
        realm_name=data.get("realm_name"),
        ruler=data.get("ruler")
    )

    db.session.add(new_realm)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to create realm"}), 400

    return jsonify(realm_schema.dump(new_realm)), 201


def get_all_realms():
    realms = db.session.query(Realms).all()
    return jsonify(realms_schema.dump(realms)), 200


def get_realm_by_id(realm_id):
    realm = db.session.query(Realms).filter(Realms.realm_id == realm_id).first()

    if not realm:
        return jsonify({"message": "Realm not found"}), 404

    return jsonify(realm_schema.dump(realm)), 200


def update_realm(realm_id):
    realm = db.session.query(Realms).filter(Realms.realm_id == realm_id).first()

    if not realm:
        return jsonify({"message": "Realm not found"}), 404

    data = request.get_json()
    populate_object(realm, data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to update realm"}), 400

    return jsonify(realm_schema.dump(realm)), 200


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
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to delete realm"}), 400

    return jsonify({"message": "Realm deleted successfully"}), 200

