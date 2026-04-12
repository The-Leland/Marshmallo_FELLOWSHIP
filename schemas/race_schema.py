



from marshmallow import Schema, fields

class RaceSchema(Schema):
    race_id = fields.UUID()
    race_name = fields.String()
    homeland = fields.String()
    lifespan = fields.Integer()
    heroes = fields.List(fields.Nested("HeroSchema"))