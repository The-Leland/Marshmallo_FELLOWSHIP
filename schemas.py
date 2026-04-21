


from models.hero import HeroSchema
from models.race import RaceSchema
from models.ability import AbilitySchema
from models.quest import QuestSchema
from models.hero_quest import HeroQuestSchema
from models.location import LocationSchema
from models.realm import RealmSchema



hero_schema = None
heroes_schema = None

race_schema = None
races_schema = None

ability_schema = None
abilities_schema = None

quest_schema = None
quests_schema = None

hero_quest_schema = None
hero_quests_schema = None

location_schema = None
locations_schema = None

realm_schema = None
realms_schema = None


def init_schemas():
    from models.hero import HeroSchema
    from models.race import RaceSchema
    from models.ability import AbilitySchema
    from models.quest import QuestSchema
    from models.hero_quest import HeroQuestSchema
    from models.location import LocationSchema
    from models.realm import RealmSchema

    global hero_schema, heroes_schema
    global race_schema, races_schema
    global ability_schema, abilities_schema
    global quest_schema, quests_schema
    global hero_quest_schema, hero_quests_schema
    global location_schema, locations_schema
    global realm_schema, realms_schema

    hero_schema = HeroSchema()
    heroes_schema = HeroSchema(many=True)

    race_schema = RaceSchema()
    races_schema = RaceSchema(many=True)

    ability_schema = AbilitySchema()
    abilities_schema = AbilitySchema(many=True)

    quest_schema = QuestSchema()
    quests_schema = QuestSchema(many=True)

    hero_quest_schema = HeroQuestSchema()
    hero_quests_schema = HeroQuestSchema(many=True)

    location_schema = LocationSchema()
    locations_schema = LocationSchema(many=True)

    realm_schema = RealmSchema()
    realms_schema = RealmSchema(many=True)
