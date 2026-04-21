


import uuid
from db import db
from db import ma


class Locations(db.Model):
    __tablename__ = "locations"

    location_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    realm_id = db.Column(db.String, db.ForeignKey("realms.realm_id"), nullable=False)
    location_name = db.Column(db.String, unique=True, nullable=False)
    danger_level = db.Column(db.Integer)


class LocationSchema(ma.Schema):
    class Meta:
        fields = (
            "location_id",
            "realm_id",
            "location_name",
            "danger_level"
        )



