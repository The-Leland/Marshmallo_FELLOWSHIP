

from marshmallow import Schema, fields

class AbilitySchema(Schema):
    ability_id = fields.UUID()
    hero_id = fields.UUID()
    ability_name = fields.String()
    power_level = fields.Integer()
    