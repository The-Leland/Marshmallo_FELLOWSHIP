


from models.reflected import Heroes, Abilities, HeroQuest, Quests
# from models.reflection_models import Quests, HeroQuest, Heroes
from schemas.quest_schema import QuestSchema
from sqlalchemy.orm import Session
from db import db

quest_schema = QuestSchema()
quests_schema = QuestSchema(many=True)

def get_all_quests():
    with Session(db.engine) as session:
        quests = session.query(Quests).all()
        return quests_schema.dump(quests)

def get_quests_by_difficulty(level):
    with Session(db.engine) as session:
        quests = session.query(Quests).filter(Quests.difficulty == level).all()
        return quests_schema.dump(quests)

def get_quest_by_id(quest_id):
    with Session(db.engine) as session:
        quest = session.get(Quests, quest_id)
        if not quest:
            return None
        return quest_schema.dump(quest)

def create_quest(data):
    with Session(db.engine) as session:
        quest = Quests(**data)
        session.add(quest)
        session.commit()
        return quest_schema.dump(quest)

def update_quest(quest_id, data):
    with Session(db.engine) as session:
        quest = session.get(Quests, quest_id)
        if not quest:
            return None
        for key, value in data.items():
            setattr(quest, key, value)
        session.commit()
        return quest_schema.dump(quest)

def complete_quest(quest_id):
    with Session(db.engine) as session:
        quest = session.get(Quests, quest_id)
        if not quest:
            return None
        quest.is_completed = True
        session.commit()
        return quest_schema.dump(quest)

def delete_quest(quest_id):
    with Session(db.engine) as session:
        quest = session.get(Quests, quest_id)
        if not quest:
            return None
        session.delete(quest)
        session.commit()
        return True
    
