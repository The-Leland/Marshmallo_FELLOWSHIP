


from flask import Blueprint, request, jsonify
from controllers.realm_controller import (
    create_realm,
    get_all_realms,
    get_realm_by_id,
    update_realm,
    delete_realm
)
from schemas.realm_schema import RealmSchema

realm_bp = Blueprint("realm_bp", __name__)
realm_schema = RealmSchema()
realm_list_schema = RealmSchema(many=True)


@realm_bp.route('/realm', methods=['POST'])
def add_realm():
    realm = create_realm(request.get_json())
    if not realm:
        return {"message": "Unable to create realm"}, 400
    return jsonify(realm_schema.dump(realm)), 201


@realm_bp.route('/realms', methods=['GET'])
def list_realms():
    realms = get_all_realms()
    return jsonify(realm_list_schema.dump(realms)), 200


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
        return {"message": "Unable to update realm"}, 400
    return jsonify(realm_schema.dump(updated)), 200


@realm_bp.route('/realm/delete/<uuid:realm_id>', methods=['DELETE'])
def delete_realm_route(realm_id):
    deleted = delete_realm(realm_id)

    if deleted is False:
        return {"message": "Cannot delete realm: locations still belong to this realm"}, 400

    if deleted is None:
        return {"message": "Realm not found"}, 404

    return jsonify(realm_schema.dump(deleted)), 200
