


import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db, ma


class Locations(db.Model):
    __tablename__ = "locations"

    location_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    realm_id = db.Column(UUID(as_uuid=True), db.ForeignKey("realms.realm_id"), nullable=False)

    location_name = db.Column(db.String(), unique=True, nullable=False)
    danger_level = db.Column(db.Integer())

    realm = db.relationship("Realms", back_populates="locations")
    quests = db.relationship("Quests", back_populates="location")

    def __init__(self, location_name, realm_id, danger_level=None):
        self.location_name = location_name
        self.realm_id = realm_id
        self.danger_level = danger_level


class LocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Locations
        load_instance = True
        include_fk = True
        include_relationships = False


location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)




