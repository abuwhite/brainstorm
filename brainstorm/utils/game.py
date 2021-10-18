"""Game module."""

from brainstorm.utils.colors import menu
from PyInquirer import prompt
from termcolor import cprint

GAMES = (
    "Calc",
    "Even",
    "Gcd",
    "Prime",
    "Progression",
)


def get_game():
    """Offer games to choose from.

    Returns:
        str: Choices game.
    """
    question = [
        {
            "type": "list",
            "name": "game",
            "message": "Choose a game:",
            "choices": GAMES,
            "filter": lambda game: game.lower(),
        },
    ]

    return prompt(
        question,
        style=menu,
    ).get("game")


def print_title(self):
    """Create title.

    Args:
        self: Other string data.
    """
    # print('-' * len(self))
    cprint(
        self,
        attrs=["reverse"],
    )
    # print('-' * len(self))
