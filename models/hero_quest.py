

import uuid
from datetime import datetime
from db import db
from db import ma


class HeroQuest(db.Model):
    __tablename__ = "hero_quest"

    hero_id = db.Column(db.String, db.ForeignKey("heroes.hero_id"), primary_key=True)
    quest_id = db.Column(db.String, db.ForeignKey("quests.quest_id"), primary_key=True)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)


class HeroQuestSchema(ma.Schema):
    class Meta:
        fields = (
            "hero_id",
            "quest_id",
            "date_joined"
        )



