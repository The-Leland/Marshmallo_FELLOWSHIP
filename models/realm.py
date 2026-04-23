

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


class RealmSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Realms
        load_instance = True
        include_fk = True
        include_relationships = False


realm_schema = RealmSchema()
realms_schema = RealmSchema(many=True)




