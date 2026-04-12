


from marshmallow import Schema, fields

class LocationSchema(Schema):
    location_id = fields.UUID()
    realm_id = fields.UUID()
    location_name = fields.String()
    danger_level = fields.Integer()
    quests = fields.List(fields.Nested("QuestSchema"))