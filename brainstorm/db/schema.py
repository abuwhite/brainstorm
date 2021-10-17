from datetime import datetime
from pony.orm import *

from brainstorm.db.models import Players


@db_session
def add_data(player_name, player_score):
    player_in_db = Players.get(name=player_name)
    if not player_in_db:
        Players(name=player_name, score=player_score)
    player = Players.get(name=player_name)
    player.score += player_score


@db_session
def show_data():
    persons = select(p for p in Players)
    persons.show()
