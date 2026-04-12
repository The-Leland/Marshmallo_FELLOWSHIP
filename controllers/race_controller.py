

from models.reflected import Heroes, Abilities, HeroQuest, Quests, Races
from schemas.race_schema import RaceSchema
from sqlalchemy.orm import Session
from db import db

race_schema = RaceSchema()
races_schema = RaceSchema(many=True)

def get_all_races():
    with Session(db.engine) as session:
        races = session.query(Races).all()
        return races_schema.dump(races)

def get_race_by_id(race_id):
    with Session(db.engine) as session:
        race = session.get(Races, race_id)
        if not race:
            return None
        return race_schema.dump(race)

def create_race(data):
    with Session(db.engine) as session:
        race = Races(**data)
        session.add(race)
        session.commit()
        return race_schema.dump(race)

def update_race(race_id, data):
    with Session(db.engine) as session:
        race = session.get(Races, race_id)
        if not race:
            return None
        for key, value in data.items():
            setattr(race, key, value)
        session.commit()
        return race_schema.dump(race)

def delete_race(race_id):
    with Session(db.engine) as session:
        heroes_exist = session.query(Heroes).filter(Heroes.race_id == race_id).first()
        if heroes_exist:
            return "blocked"
        race = session.get(Races, race_id)
        if not race:
            return None
        session.delete(race)
        session.commit()
        return True
    