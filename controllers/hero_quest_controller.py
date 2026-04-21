


from db import db
from models.hero_quest import HeroQuest
from models.hero import Heroes
from models.quest import Quests


def create_hero_quest(data):
    record = HeroQuest(
        hero_id=data.get("hero_id"),
        quest_id=data.get("quest_id")
    )
    db.session.add(record)
    db.session.commit()
    return record


def get_all_hero_quests():
    return db.session.query(HeroQuest).all()


def get_hero_quest(hero_id, quest_id):
    return (
        db.session.query(HeroQuest)
        .filter_by(hero_id=hero_id, quest_id=quest_id)
        .first()
    )


def update_hero_quest(hero_id, quest_id, data):
    record = (
        db.session.query(HeroQuest)
        .filter_by(hero_id=hero_id, quest_id=quest_id)
        .first()
    )
    if not record:
        return None

    for key, value in data.items():
        setattr(record, key, value)

    db.session.commit()
    return record


def delete_hero_quest(hero_id, quest_id):
    record = (
        db.session.query(HeroQuest)
        .filter_by(hero_id=hero_id, quest_id=quest_id)
        .first()
    )
    if not record:
        return None

    db.session.delete(record)
    db.session.commit()
    return True


def get_quests_by_hero(hero_id):
    return (
        db.session.query(Quests)
        .join(HeroQuest, HeroQuest.quest_id == Quests.quest_id)
        .filter(HeroQuest.hero_id == hero_id)
        .all()
    )


def get_heroes_by_quest(quest_id):
    return (
        db.session.query(Heroes)
        .join(HeroQuest, HeroQuest.hero_id == Heroes.hero_id)
        .filter(HeroQuest.quest_id == quest_id)
        .all()
    )
