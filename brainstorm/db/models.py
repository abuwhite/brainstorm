from datetime import datetime
from pony.orm import *

from brainstorm.config import db_params

db = Database()


class Players(db.Entity):
    name = Required(str)
    score = Required(int)


# sql_debug(True)
db.bind(**db_params)
db.generate_mapping(create_tables=True)
