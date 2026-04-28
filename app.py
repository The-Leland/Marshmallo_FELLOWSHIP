


from flask import Flask
from db import db, init_db
from utils.blueprints import register_blueprints

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://L27Fe:Test123!@localhost:5432/Marshmallo_FELLOWSHIP"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


import models.realm
import models.location
import models.race
import models.hero
import models.ability
import models.quest
import models.hero_quest


init_db(app, db)


register_blueprints(app)

@app.route('/')
def index():
    return {"message": "Welcome to the Fellowship Management API"}

if __name__ == '__main__':
    app.run(debug=True)




