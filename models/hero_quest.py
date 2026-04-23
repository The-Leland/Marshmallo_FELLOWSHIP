

import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db, ma


class HeroQuest(db.Model):
    __tablename__ = "hero_quest"

    hero_id = db.Column(UUID(as_uuid=True), db.ForeignKey("heroes.hero_id"), primary_key=True)
    quest_id = db.Column(UUID(as_uuid=True), db.ForeignKey("quests.quest_id"), primary_key=True)
    date_joined = db.Column(db.DateTime())

    hero = db.relationship("Heroes", back_populates="quests")
    quest = db.relationship("Quests", back_populates="heroes")

    def __init__(self, hero_id, quest_id, date_joined=None):
        self.hero_id = hero_id
        self.quest_id = quest_id
        self.date_joined = date_joined


class HeroQuestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HeroQuest
        load_instance = True
        include_fk = True
        include_relationships = False


hero_quest_schema = HeroQuestSchema()
hero_quests_schema = HeroQuestSchema(many=True)






