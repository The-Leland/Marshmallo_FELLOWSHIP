


import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db, ma


class Races(db.Model):
    __tablename__ = "races"

    race_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    race_name = db.Column(db.String(), unique=True, nullable=False)
    homeland = db.Column(db.String())
    lifespan = db.Column(db.Integer())

    heroes = db.relationship("Heroes", back_populates="race")

    def __init__(self, race_name, homeland=None, lifespan=None):
        self.race_name = race_name
        self.homeland = homeland
        self.lifespan = lifespan

def new_race(data):
    return Races(
        race_name=data.get("race_name"),
        homeland=data.get("homeland"),
        lifespan=data.get("lifespan")
    )

def race_schema():
    from .hero import hero_schema

    class RaceSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Races
            load_instance = True
            include_fk = True
            include_relationships = False

        heroes = ma.Nested(hero_schema().__class__, many=True)

    return RaceSchema()

def races_schema():
    from .hero import hero_schema

    class RaceSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Races
            load_instance = True
            include_fk = True
            include_relationships = False

        heroes = ma.Nested(hero_schema().__class__, many=True)

    return RaceSchema(many=True)
