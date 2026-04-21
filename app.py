
from flask import Flask
from db import init_db
from utils.blueprints import register_blueprints


import models.hero
import models.race
import models.ability
import models.quest
import models.hero_quest
import models.location
import models.realm

app = Flask(__name__)


init_db(app)
register_blueprints(app)

@app.route('/')
def index():
    return {"message": "Welcome to the Fellowship Management API"}

if __name__ == '__main__':
    app.run(debug=True)
