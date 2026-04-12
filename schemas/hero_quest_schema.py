



from marshmallow import Schema, fields

class HeroQuestSchema(Schema):
    hero_id = fields.UUID()
    quest_id = fields.UUID()
    date_joined = fields.DateTime()
