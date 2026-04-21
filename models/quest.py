


import uuid
from db import db
from db import ma


class Quests(db.Model):
    __tablename__ = "quests"

    quest_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    location_id = db.Column(db.String, db.ForeignKey("locations.location_id"), nullable=False)
    quest_name = db.Column(db.String, unique=True, nullable=False)
    difficulty = db.Column(db.String)
    reward_gold = db.Column(db.Integer)
    is_completed = db.Column(db.Boolean, default=False)

    hero_quests = db.relationship("HeroQuest", backref="quest", lazy=True)


class QuestSchema(ma.Schema):
    class Meta:
        fields = (
            "quest_id",
            "location_id",
            "quest_name",
            "difficulty",
            "reward_gold",
            "is_completed"
        )



