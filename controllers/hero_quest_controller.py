


from models.reflected import HeroQuest, Heroes, Quests
from schemas.hero_quest_schema import HeroQuestSchema
from sqlalchemy.orm import Session
from db import db

hero_quest_schema = HeroQuestSchema()
hero_quests_schema = HeroQuestSchema(many=True)

def create_hero_quest(data):
    with Session(db.engine) as session:
        record = HeroQuest(**data)
        session.add(record)
        session.commit()
        return hero_quest_schema.dump(record)

def get_all_hero_quests():
    with Session(db.engine) as session:
        assignments = session.query(HeroQuest).all()
        return hero_quests_schema.dump(assignments)

def get_hero_quest(hero_quest_id):
    with Session(db.engine) as session:
        record = session.get(HeroQuest, hero_quest_id)
        if not record:
            return None
        return hero_quest_schema.dump(record)

def delete_hero_quest(hero_quest_id):
    with Session(db.engine) as session:
        record = session.get(HeroQuest, hero_quest_id)
        if not record:
            return None
        session.delete(record)
        session.commit()
        return True


def update_hero_quest(hero_quest_id, data):
    with Session(db.engine) as session:
        record = session.get(HeroQuest, hero_quest_id)
        if not record:
            return None

        for key, value in data.items():
            setattr(record, key, value)

        session.commit()
        return hero_quest_schema.dump(record)
    

def get_quests_by_hero(hero_id):
    with Session(db.engine) as session:
        results = (
            session.query(Quests)
            .join(HeroQuest, HeroQuest.quest_id == Quests.quest_id)
            .filter(HeroQuest.hero_id == hero_id)
            .all()
        )
        return [q.quest_id for q in results]  


def get_heroes_by_quest(quest_id):
    with Session(db.engine) as session:
        results = (
            session.query(Heroes)
            .join(HeroQuest, HeroQuest.hero_id == Heroes.hero_id)
            .filter(HeroQuest.quest_id == quest_id)
            .all()
        )
        return [h.hero_id for h in results]  