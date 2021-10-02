"""Config module."""

import types

from oasis.games import calc, even, gcd, prime, progression
from oasis.games.list import GAMES

NUMBER_ROUNDS = 3  # The number of rounds in the game.

MODULES = types.MappingProxyType(
    {
        'calc': calc,
        "even": even,
        "gcd": gcd,
        "prime": prime,
        "progression": progression,
    },
)

ASK_NAME = [
    {
        'type': "input",
        'name': "player",
        'message': "What's your name:",
    },
]

LIST_GAMES = [
    {
        'type': 'list',
        'name': 'game',
        'message': 'Choose a game:',
        'choices': GAMES,
        'filter': lambda val: val.lower()
    },
]


MENU = [
    {
        'type': 'list',
        'name': 'menu',
        'message': 'Menu',
        'choices': ['Play', 'Help', 'Exit'],
        'filter': lambda val: val.lower()
    },
]
