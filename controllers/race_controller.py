

from db import db
from models.race import Races
from models.hero import Heroes


def get_all_races():
    return db.session.query(Races).all()


def get_race_by_id(race_id):
    return db.session.query(Races).filter_by(race_id=race_id).first()


def create_race(data):
    race = Races(
        race_name=data.get("race_name"),
        homeland=data.get("homeland"),
        lifespan=data.get("lifespan")
    )
    db.session.add(race)
    db.session.commit()
    return race


def update_race(race_id, data):
    race = db.session.query(Races).filter_by(race_id=race_id).first()
    if not race:
        return None

    for key, value in data.items():
        setattr(race, key, value)

    db.session.commit()
    return race


def delete_race(race_id):
    hero_exists = db.session.query(Heroes).filter_by(race_id=race_id).first()
    if hero_exists:
        return "blocked"

    race = db.session.query(Races).filter_by(race_id=race_id).first()
    if not race:
        return None

    db.session.delete(race)
    db.session.commit()
    return True
