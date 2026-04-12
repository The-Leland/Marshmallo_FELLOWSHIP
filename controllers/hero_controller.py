

from models.reflected import Heroes, Abilities, HeroQuest, Quests
from schemas.hero_schema import HeroSchema
from schemas.quest_schema import QuestSchema
from schemas.ability_schema import AbilitySchema
from sqlalchemy.orm import Session
from db import db

hero_schema = HeroSchema()
heroes_schema = HeroSchema(many=True)
quest_schema = QuestSchema(many=True)
ability_schema = AbilitySchema(many=True)

def get_all_heroes():
    with Session(db.engine) as session:
        heroes = session.query(Heroes).all()
        return heroes

def get_alive_heroes():
    with Session(db.engine) as session:
        return session.query(Heroes).filter(Heroes.is_alive == True).all()

def get_hero_by_id(hero_id):
    with Session(db.engine) as session:
        hero = session.get(Heroes, hero_id)
        if not hero:
            return None
        return hero_schema.dump(hero)

def get_hero_quests(hero_id):
    with Session(db.engine) as session:
        quests = (
            session.query(Quests)
            .join(HeroQuest, HeroQuest.quest_id == Quests.quest_id)
            .filter(HeroQuest.hero_id == hero_id)
            .all()
        )
        return quest_schema.dump(quests)

def create_hero(data):
    with Session(db.engine) as session:
        hero = Heroes(**data)
        session.add(hero)
        session.commit()
        return hero_schema.dump(hero)

def update_hero(hero_id, data):
    with Session(db.engine) as session:
        hero = session.get(Heroes, hero_id)
        if not hero:
            return None
        for key, value in data.items():
            setattr(hero, key, value)
        session.commit()
        return hero_schema.dump(hero)

def delete_hero(hero_id):
    with Session(db.engine) as session:
        hero = session.get(Heroes, hero_id)
        if not hero:
            return None
        session.delete(hero)
        session.commit()
        return True
    
