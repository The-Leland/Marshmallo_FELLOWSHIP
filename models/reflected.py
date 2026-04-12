

# Heroes = None
# Races = None
# Realms = None
# Locations = None
# Quests = None
# Abilities = None
# HeroQuest = None



from models.reflection_models import reflect

classes = reflect()

Heroes = classes.heroes
Races = classes.races
Realms = classes.realms
Locations = classes.locations
Quests = classes.quests
Abilities = classes.abilities
HeroQuest = classes.hero_quest