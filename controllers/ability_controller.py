


from db import db
from models.ability import Abilities
from models.hero import Heroes


def get_all_abilities():
    return db.session.query(Abilities).all()


def get_ability_by_id(ability_id):
    return db.session.query(Abilities).filter_by(ability_id=ability_id).first()


def create_ability(data):
    ability = Abilities(
        hero_id=data.get("hero_id"),
        ability_name=data.get("ability_name"),
        power_level=data.get("power_level")
    )
    db.session.add(ability)
    db.session.commit()
    return ability


def update_ability(ability_id, data):
    ability = db.session.query(Abilities).filter_by(ability_id=ability_id).first()
    if not ability:
        return None

    for key, value in data.items():
        setattr(ability, key, value)

    db.session.commit()
    return ability


def delete_ability(ability_id):
    ability = db.session.query(Abilities).filter_by(ability_id=ability_id).first()
    if not ability:
        return None

    db.session.delete(ability)
    db.session.commit()
    return True

