


from flask import Blueprint
from controllers.hero_controller import (
    add_hero,
    get_all_heroes,
    get_hero_by_id,
    update_hero,
    delete_hero,
    get_alive_heroes
)

hero_bp = Blueprint("hero_bp", __name__)


@hero_bp.route("/hero", methods=["POST"])
def route_add_hero():
    return add_hero()


@hero_bp.route("/heroes", methods=["GET"])
def route_get_all_heroes():
    return get_all_heroes()


@hero_bp.route("/hero/<uuid:hero_id>", methods=["GET"])
def route_get_hero_by_id(hero_id):
    return get_hero_by_id(hero_id)


@hero_bp.route("/hero/<uuid:hero_id>", methods=["PUT"])
def route_update_hero(hero_id):
    return update_hero(hero_id)


@hero_bp.route("/hero/<uuid:hero_id>", methods=["DELETE"])
def route_delete_hero(hero_id):
    return delete_hero(hero_id)


@hero_bp.route("/heroes/alive", methods=["GET"])
def route_get_alive_heroes():
    return get_alive_heroes()
