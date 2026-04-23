
from flask import Blueprint
from controllers.ability_controller import (
    add_ability,
    get_all_abilities,
    get_ability_by_id,
    update_ability,
    delete_ability
)

ability_bp = Blueprint("ability_bp", __name__)


@ability_bp.route("/ability", methods=["POST"])
def route_add_ability():
    return add_ability()


@ability_bp.route("/abilities", methods=["GET"])
def route_get_all_abilities():
    return get_all_abilities()


@ability_bp.route("/ability/<uuid:ability_id>", methods=["GET"])
def route_get_ability_by_id(ability_id):
    return get_ability_by_id(ability_id)


@ability_bp.route("/ability/<uuid:ability_id>", methods=["PUT"])
def route_update_ability(ability_id):
    return update_ability(ability_id)


@ability_bp.route("/ability/<uuid:ability_id>", methods=["DELETE"])
def route_delete_ability(ability_id):
    return delete_ability(ability_id)
