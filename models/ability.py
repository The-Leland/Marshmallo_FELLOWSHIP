


import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db, ma


class Abilities(db.Model):
    __tablename__ = "abilities"

    ability_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    hero_id = db.Column(UUID(as_uuid=True), db.ForeignKey("heroes.hero_id"), nullable=False)

    ability_name = db.Column(db.String(), unique=True, nullable=False)
    power_level = db.Column(db.Integer())

    hero = db.relationship("Heroes", back_populates="abilities")

    def __init__(self, ability_name, hero_id, power_level=None):
        self.ability_name = ability_name
        self.hero_id = hero_id
        self.power_level = power_level


def ability_schema():
    class AbilitySchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Abilities
            load_instance = True
            include_fk = True
            include_relationships = False
    return AbilitySchema()

def abilities_schema():
    class AbilitySchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Abilities
            load_instance = True
            include_fk = True
            include_relationships = False
    return AbilitySchema(many=True)


