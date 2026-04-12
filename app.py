
# from flask import Flask
# from models import reflection_models
# from utils.blueprints import register_blueprints
# import sys, os

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# app = Flask(__name__)
# register_blueprints(app)

# @app.route('/')
# def index():
#     return {"message": "Welcome to the Fellowship Management API"}

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask
from db import init_db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://L27Fe:Test123!@localhost:5432/Marshmallo_FELLOWSHIP"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app)

with app.app_context():
    from models.reflection_models import reflect
    from models import reflected

    classes = reflect()

    reflected.Heroes = classes.heroes
    reflected.Races = classes.races
    reflected.Realms = classes.realms
    reflected.Locations = classes.locations
    reflected.Quests = classes.quests
    reflected.Abilities = classes.abilities
    reflected.HeroQuest = classes.hero_quest

from utils.blueprints import register_blueprints
register_blueprints(app)

@app.route('/')
def index():
    return {"message": "Welcome to the Fellowship Management API"}

if __name__ == '__main__':
    app.run(debug=True)