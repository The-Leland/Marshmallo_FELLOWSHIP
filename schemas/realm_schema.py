


from marshmallow import Schema, fields

class RealmSchema(Schema):
    realm_id = fields.UUID()
    realm_name = fields.String()
    ruler = fields.String()
    locations = fields.List(fields.Nested("LocationSchema"))

    