


import uuid
from db import db
from db import ma


class Races(db.Model):
    __tablename__ = "races"

    race_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    race_name = db.Column(db.String, unique=True, nullable=False)
    homeland = db.Column(db.String)
    lifespan = db.Column(db.Integer)

    heroes = db.relationship("Heroes", backref="race", lazy=True)


class RaceSchema(ma.Schema):
    class Meta:
        fields = (
            "race_id",
            "race_name",
            "homeland",
            "lifespan"
        )



