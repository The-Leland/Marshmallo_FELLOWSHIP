


from db import db
from models.quest import Quests
from models.hero_quest import HeroQuest
from models.hero import Heroes


def get_all_quests():
    return db.session.query(Quests).all()


def get_quests_by_difficulty(level):
    return db.session.query(Quests).filter_by(difficulty=level).all()


def get_quest_by_id(quest_id):
    return db.session.query(Quests).filter_by(quest_id=quest_id).first()


def create_quest(data):
    quest = Quests(
        location_id=data.get("location_id"),
        quest_name=data.get("quest_name"),
        difficulty=data.get("difficulty"),
        reward_gold=data.get("reward_gold"),
        is_completed=data.get("is_completed", False)
    )
    db.session.add(quest)
    db.session.commit()
    return quest


def update_quest(quest_id, data):
    quest = db.session.query(Quests).filter_by(quest_id=quest_id).first()
    if not quest:
        return None

    for key, value in data.items():
        setattr(quest, key, value)

    db.session.commit()
    return quest


def complete_quest(quest_id):
    quest = db.session.query(Quests).filter_by(quest_id=quest_id).first()
    if not quest:
        return None

    quest.is_completed = True
    db.session.commit()
    return quest


def delete_quest(quest_id):
    quest = db.session.query(Quests).filter_by(quest_id=quest_id).first()
    if not quest:
        return None

    db.session.delete(quest)
    db.session.commit()
    return True

