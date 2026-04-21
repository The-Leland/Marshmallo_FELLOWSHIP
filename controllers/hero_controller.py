


from db import db
from models.hero import Heroes
from models.quest import Quests
from models.ability import Abilities
from models.hero_quest import HeroQuest


def get_all_heroes():
    return db.session.query(Heroes).all()


def get_alive_heroes():
    return db.session.query(Heroes).filter_by(is_alive=True).all()


def get_hero_by_id(hero_id):
    return db.session.query(Heroes).filter_by(hero_id=hero_id).first()


def get_hero_quests(hero_id):
    return (
        db.session.query(Quests)
        .join(HeroQuest, HeroQuest.quest_id == Quests.quest_id)
        .filter(HeroQuest.hero_id == hero_id)
        .all()
    )


def create_hero(data):
    hero = Heroes(
        race_id=data.get("race_id"),
        hero_name=data.get("hero_name"),
        age=data.get("age"),
        health_points=data.get("health_points"),
        is_alive=data.get("is_alive", True)
    )
    db.session.add(hero)
    db.session.commit()
    return hero


def update_hero(hero_id, data):
    hero = db.session.query(Heroes).filter_by(hero_id=hero_id).first()
    if not hero:
        return None

    for key, value in data.items():
        setattr(hero, key, value)

    db.session.commit()
    return hero


def delete_hero(hero_id):
    hero = db.session.query(Heroes).filter_by(hero_id=hero_id).first()
    if not hero:
        return None

    db.session.delete(hero)
    db.session.commit()
    return True
