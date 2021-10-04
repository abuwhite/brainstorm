"""Menu module."""

from oasis.utils.colors import style1
from PyInquirer import prompt


class MainMenu(object):
    """Menu class. State buttons."""

    def __init__(self, answer):
        """Init menu.

        Args:
            answer: Dict menu
        """
        self._play = False
        self._stats = False
        self._exit = False

        button = answer.get("menu")

        if button == "play":
            self._play = True
        elif button == "stats":
            self._stats = True
        elif button == "exit":
            self._exit = True

    @property
    def play(self):
        """Get play.

        Returns:
            bool: Play
        """
        return self._play

    @property
    def stats(self):
        """Get stats.

        Returns:
            bool: Stats
        """
        return self._stats

    @property
    def exit(self):
        """Get stats.

        Returns:
            bool: Exit
        """
        return self._exit


def get_menu():
    """Get menu.

    Returns:
        class: MainMenu
    """
    menu = [
        {
            "type": "list",
            "name": "menu",
            "message": "Menu",
            "choices": ["Play", "Stats", "Exit"],
            "filter": lambda game: game.lower(),
        },
    ]

    return MainMenu(
        prompt(
            menu,
            style=style1,
        ),
    )
