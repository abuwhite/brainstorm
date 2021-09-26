"""Config module."""


from oasis.games import calc, even, gcd, prime, progression

NUMBER_ROUNDS = 3  # The number of rounds in the game.

GAMES = [
    '0) Calc',
    '1) Even',
    '2) Gcd',
    '3) Prime',
    '4) Progression'
]

MODULES = {
    0: calc,
    1: even,
    2: gcd,
    3: prime,
    4: progression
}
