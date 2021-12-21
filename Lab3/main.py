from view import Menu
from db import Base, engine
from sqlalchemy import *
metadata = MetaData()

Base.metadata.create_all(engine)

Menu.mainmenu()
