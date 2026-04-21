



from flask import Blueprint, request, jsonify
from controllers.realm_controller import (
    create_realm,
    get_all_realms,
    get_realm_by_id,
    update_realm,
    delete_realm
)
from models.realm import RealmSchema 

realm_bp = Blueprint("realm_bp", __name__)


@realm_bp.route('/realm', methods=['POST'])
def add_realm():
    realm = create_realm(request.get_json())
    return jsonify(RealmSchema().dump(realm)), 201 


@realm_bp.route('/realms', methods=['GET'])
def list_realms():
    realms = get_all_realms()
    return jsonify(RealmSchema(many=True).dump(realms)), 200 


@realm_bp.route('/realm/<uuid:realm_id>', methods=['GET'])
def get_single_realm(realm_id):
    realm = get_realm_by_id(realm_id)
    if not realm:
        return {"message": "Realm not found"}, 404
    return jsonify(realm_schema.dump(realm)), 200


@realm_bp.route('/realm/<uuid:realm_id>', methods=['PUT'])
def update_realm_route(realm_id):
    updated = update_realm(realm_id, request.get_json())
    if not updated:
        return {"message": "Realm not found"}, 404
    return jsonify(realm_schema.dump(updated)), 200


@realm_bp.route('/realm/<uuid:realm_id>', methods=['DELETE'])
def delete_realm_route(realm_id):
    deleted = delete_realm(realm_id)

    if deleted == "blocked":
        return {"message": "Cannot delete realm: locations still belong to this realm"}, 400

    if deleted is None:
        return {"message": "Realm not found"}, 404

    return {"message": "Realm deleted successfully"}, 200

