"""Player module."""

from brainstorm.utils.colors import style1, style3
from PyInquirer import prompt


def is_ready():
    """Check player ready.

    Returns:
        bool: True if Player ready else False
    """
    question = [
        {
            "type": "confirm",
            "message": "Are you ready?",
            "name": "continue",
            "default": True,
        },
    ]

    return prompt(
        question,
        style=style1,
    ).get("continue")


def get_name():
    """Ask for the player's name.

    Returns:
        str: Player name
    """
    question = [
        {
            "type": "input",
            "name": "player",
            "message": "What's your name:",
        },
    ]

    return prompt(
        question,
        style=style3,
    ).get("player")
