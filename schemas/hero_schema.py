


from marshmallow import Schema, fields

class HeroSchema(Schema):
    hero_id = fields.UUID()
    race_id = fields.UUID()
    hero_name = fields.String()
    age = fields.Integer()
    health_points = fields.Integer()
    is_alive = fields.Boolean()
    abilities = fields.List(fields.Nested("AbilitySchema"))
    quests = fields.List(fields.Nested("QuestSchema"))