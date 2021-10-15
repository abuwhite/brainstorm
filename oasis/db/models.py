from datetime import datetime
from pony.orm import *

db = Database()


class Players(db.Entity):
    name = Required(str)
    score = Required(int)

# sql_debug(True)
db.bind(provider='sqlite', filename='stats', create_db=True)
db.generate_mapping(create_tables=True)