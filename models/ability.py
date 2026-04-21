


import uuid
from db import db
from db import ma


class Abilities(db.Model):
    __tablename__ = "abilities"

    ability_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    hero_id = db.Column(db.String, db.ForeignKey("heroes.hero_id"), nullable=False)
    ability_name = db.Column(db.String, unique=True, nullable=False)
    power_level = db.Column(db.Integer)


class AbilitySchema(ma.Schema):
    class Meta:
        fields = (
            "ability_id",
            "hero_id",
            "ability_name",
            "power_level"
        )



