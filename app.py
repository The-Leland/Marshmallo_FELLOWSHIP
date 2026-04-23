
from flask import Flask
from db import db, init_db
from utils.blueprints import register_blueprints

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://L27Fe:Test123!@localhost:5432/Marshmallo_FELLOWSHIP"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)

from models import hero, race, ability, quest, hero_quest, location, realm

register_blueprints(app)

@app.route('/')
def index():
    return {"message": "Welcome to the Fellowship Management API"}

if __name__ == '__main__':
    app.run(debug=True)


