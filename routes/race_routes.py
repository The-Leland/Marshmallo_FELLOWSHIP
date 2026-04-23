


from flask import Blueprint
from controllers.race_controller import (
    add_race,
    get_all_races,
    get_race_by_id,
    update_race,
    delete_race
)

race_bp = Blueprint("race_bp", __name__)


@race_bp.route("/race", methods=["POST"])
def route_add_race():
    return add_race()


@race_bp.route("/races", methods=["GET"])
def route_get_all_races():
    return get_all_races()


@race_bp.route("/race/<uuid:race_id>", methods=["GET"])
def route_get_race_by_id(race_id):
    return get_race_by_id(race_id)


@race_bp.route("/race/<uuid:race_id>", methods=["PUT"])
def route_update_race(race_id):
    return update_race(race_id)


@race_bp.route("/race/<uuid:race_id>", methods=["DELETE"])
def route_delete_race(race_id):
    return delete_race(race_id)
