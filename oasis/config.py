"""Config module."""

import types

from oasis.games import calc, even, gcd, prime, progression

NUMBER_ROUNDS = 3  # The number of rounds in the game.

NEWLINE = "\n"
TEXT_WIDTH = 50
BOLD = "bold"

MODULES = types.MappingProxyType(
    {
        "calc": calc,
        "even": even,
        "gcd": gcd,
        "prime": prime,
        "progression": progression,
    },
)
