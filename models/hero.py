


import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db, ma


class Heroes(db.Model):
    __tablename__ = "heroes"

    hero_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    race_id = db.Column(UUID(as_uuid=True), db.ForeignKey("races.race_id"), nullable=False)
    hero_name = db.Column(db.String(), unique=True, nullable=False)
    age = db.Column(db.Integer())
    health_points = db.Column(db.Integer(), default=100)
    is_alive = db.Column(db.Boolean(), default=True)

    race = db.relationship("Races", back_populates="heroes")
    abilities = db.relationship("Abilities", back_populates="hero")
    hero_quests = db.relationship("HeroQuests", back_populates="hero")

    def __init__(self, hero_name, race_id, age=None, health_points=100, is_alive=True):
        self.hero_name = hero_name
        self.race_id = race_id
        self.age = age
        self.health_points = health_points
        self.is_alive = is_alive

def new_hero(data):
    return Heroes(
        hero_name=data.get("hero_name"),
        race_id=data.get("race_id"),
        age=data.get("age"),
        health_points=data.get("health_points", 100),
        is_alive=data.get("is_alive", True)
    )

def hero_schema():
    from .ability import ability_schema

    class HeroSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Heroes
            load_instance = True
            include_fk = True
            include_relationships = False

        abilities = ma.Nested(ability_schema().__class__, many=True)

    return HeroSchema()

def heroes_schema():
    from .ability import ability_schema

    class HeroSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Heroes
            load_instance = True
            include_fk = True
            include_relationships = False

        abilities = ma.Nested(ability_schema().__class__, many=True)

    return HeroSchema(many=True)

