



from marshmallow import Schema, fields

class QuestSchema(Schema):
    quest_id = fields.UUID()
    location_id = fields.UUID()
    quest_name = fields.String()
    difficulty = fields.String()
    reward_gold = fields.Integer()
    is_completed = fields.Boolean()
    heroes = fields.List(fields.Nested("HeroSchema"))
    location = fields.Nested("LocationSchema")