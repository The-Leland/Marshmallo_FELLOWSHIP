


import uuid
from db import db
from db import ma


class Heroes(db.Model):
    __tablename__ = "heroes"

    hero_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    race_id = db.Column(db.String, db.ForeignKey("races.race_id"), nullable=False)
    hero_name = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer)
    health_points = db.Column(db.Integer)
    is_alive = db.Column(db.Boolean, default=True)

    abilities = db.relationship("Abilities", backref="hero", lazy=True)
    hero_quests = db.relationship("HeroQuest", backref="hero", lazy=True)


class HeroSchema(ma.Schema):
    class Meta:
        fields = (
            "hero_id",
            "race_id",
            "hero_name",
            "age",
            "health_points",
            "is_alive"
        )


