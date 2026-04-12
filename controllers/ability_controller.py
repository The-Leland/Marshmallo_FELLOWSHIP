


from models.reflected import Heroes, Abilities, HeroQuest, Quests
# from models.reflection_models import Abilities
from schemas.ability_schema import AbilitySchema
from sqlalchemy.orm import Session
from db import db

ability_schema = AbilitySchema()
abilities_schema = AbilitySchema(many=True)

def get_all_abilities():
    with Session(db.engine) as session:
        abilities = session.query(Abilities).all()
        return abilities_schema.dump(abilities)

def get_ability_by_id(ability_id):
    with Session(db.engine) as session:
        ability = session.get(Abilities, ability_id)
        if not ability:
            return None
        return ability_schema.dump(ability)

def create_ability(data):
    with Session(db.engine) as session:
        ability = Abilities(**data)
        session.add(ability)
        session.commit()
        return ability_schema.dump(ability)

def update_ability(ability_id, data):
    with Session(db.engine) as session:
        ability = session.get(Abilities, ability_id)
        if not ability:
            return None
        for key, value in data.items():
            setattr(ability, key, value)
        session.commit()
        return ability_schema.dump(ability)

def delete_ability(ability_id):
    with Session(db.engine) as session:
        ability = session.get(Abilities, ability_id)
        if not ability:
            return None
        session.delete(ability)
        session.commit()
        return True
    