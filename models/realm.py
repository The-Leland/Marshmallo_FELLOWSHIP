

import uuid
from db import db
from db import ma


class Realms(db.Model):
    __tablename__ = "realms"

    realm_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    realm_name = db.Column(db.String, unique=True, nullable=False)
    ruler = db.Column(db.String)

    locations = db.relationship("Locations", backref="realm", lazy=True)


class RealmSchema(ma.Schema):
    class Meta:
        fields = (
            "realm_id",
            "realm_name",
            "ruler"
        )



