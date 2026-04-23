


import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db, ma


class Heroes(db.Model):
    __tablename__ = "heroes"

    hero_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    race_id = db.Column(UUID(as_uuid=True), db.ForeignKey("races.race_id"), nullable=False)

    hero_name = db.Column(db.String(), unique=True, nullable=False)
    age = db.Column(db.Integer())
    health_points = db.Column(db.Integer())
    is_alive = db.Column(db.Boolean(), default=True)

    race = db.relationship("Races", back_populates="heroes")
    abilities = db.relationship("Abilities", back_populates="hero", cascade="all, delete-orphan")
    quests = db.relationship("HeroQuest", back_populates="hero", cascade="all, delete-orphan")

    def __init__(self, hero_name, race_id, age=None, health_points=None, is_alive=True):
        self.hero_name = hero_name
        self.race_id = race_id
        self.age = age
        self.health_points = health_points
        self.is_alive = is_alive


class HeroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Heroes
        load_instance = True
        include_fk = True
        include_relationships = False


hero_schema = HeroSchema()
heroes_schema = HeroSchema(many=True)


