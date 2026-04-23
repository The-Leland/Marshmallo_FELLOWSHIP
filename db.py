

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def init_db(app, db_instance=db):
    db_instance.init_app(app)
    ma.init_app(app)
