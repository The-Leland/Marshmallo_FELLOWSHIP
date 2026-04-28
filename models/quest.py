


import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db, ma


class Quests(db.Model):
    __tablename__ = "quests"

    quest_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    location_id = db.Column(UUID(as_uuid=True), db.ForeignKey("locations.location_id"), nullable=False)

    quest_name = db.Column(db.String(), unique=True, nullable=False)
    difficulty = db.Column(db.String())
    reward_gold = db.Column(db.Integer())
    is_completed = db.Column(db.Boolean(), default=False)

    location = db.relationship("Locations", back_populates="quests")
    heroes = db.relationship("HeroQuest", back_populates="quest", cascade="all, delete-orphan")

    def __init__(self, quest_name, location_id, difficulty=None, reward_gold=None, is_completed=False):
        self.quest_name = quest_name
        self.location_id = location_id
        self.difficulty = difficulty
        self.reward_gold = reward_gold
        self.is_completed = is_completed


def quest_schema():
    class QuestSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Quests
            load_instance = True
            include_fk = True
            include_relationships = False
    return QuestSchema()

def quests_schema():
    class QuestSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Quests
            load_instance = True
            include_fk = True
            include_relationships = False
    return QuestSchema(many=True)


