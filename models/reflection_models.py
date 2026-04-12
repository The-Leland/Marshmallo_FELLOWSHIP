

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData
from db import db

def reflect():
    Base = automap_base()

    metadata = MetaData()
    metadata.reflect(bind=db.engine)

    Base.metadata = metadata

    Base.prepare()
    print(Base.classes.keys())

    return Base.classes