


import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db, ma


class Realms(db.Model):
    __tablename__ = "realms"

    realm_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    realm_name = db.Column(db.String(), unique=True, nullable=False)
    ruler = db.Column(db.String())

    locations = db.relationship("Locations", back_populates="realm")

    def __init__(self, realm_name, ruler=None):
        self.realm_name = realm_name
        self.ruler = ruler

def new_realm(data):
    return Realms(
        realm_name=data.get("realm_name"),
        ruler=data.get("ruler")
    )

def realm_schema():
    from .location import location_schema

    class RealmSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Realms
            load_instance = True
            include_fk = True
            include_relationships = False

        locations = ma.Nested(location_schema().__class__, many=True)

    return RealmSchema()

def realms_schema():
    from .location import location_schema

    class RealmSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Realms
            load_instance = True
            include_fk = True
            include_relationships = False

        locations = ma.Nested(location_schema().__class__, many=True)

    return RealmSchema(many=True)



