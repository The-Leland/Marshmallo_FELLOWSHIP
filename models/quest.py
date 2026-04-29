


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
    hero_quests = db.relationship("HeroQuests", back_populates="quest")

    def __init__(self, quest_name, location_id, difficulty=None, reward_gold=None, is_completed=False):
        self.quest_name = quest_name
        self.location_id = location_id
        self.difficulty = difficulty
        self.reward_gold = reward_gold
        self.is_completed = is_completed

def new_quest(data):
    return Quests(
        quest_name=data.get("quest_name"),
        location_id=data.get("location_id"),
        difficulty=data.get("difficulty"),
        reward_gold=data.get("reward_gold"),
        is_completed=data.get("is_completed", False)
    )

def quest_schema():
    from .hero_quest import hero_quests_schema

    class QuestSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Quests
            load_instance = True
            include_fk = True
            include_relationships = False

        hero_quests = ma.Nested(hero_quests_schema().__class__, many=True)

    return QuestSchema()

def quests_schema():
    from .hero_quest import hero_quests_schema

    class QuestSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Quests
            load_instance = True
            include_fk = True
            include_relationships = False

        hero_quests = ma.Nested(hero_quests_schema().__class__, many=True)

    return QuestSchema(many=True)


