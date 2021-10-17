# -*- coding: utf-8 -*-

"""Main module."""

import cmd
from pony.orm import *

from brainstorm.config import MODULES, NEWLINE
from brainstorm.scripts import engine
from brainstorm.scripts.cli import user
from brainstorm.utils import game, player
from brainstorm.utils.menu import get_menu
from termcolor import colored

from brainstorm.db.models import Players


class GameShell(cmd.Cmd):
    """Game Shell."""

    intro = colored("Press [ENTER] to start", attrs=["reverse"])

    prompt = "> "

    def emptyline(self):
        """Start the engine after pressing the ENTER button.

        Returns:
            object: Menu function.
        """
        if self.prompt:
            return self.do_menu(self)

    def default(self, line):
        """Get default method.

        Args:
            line: Default line.
        """
        print("I do not understand that command.")
        print("Type help or ? to list commands.\n")

    @staticmethod
    def do_menu(self):
        """Get menu.

        Args:
            self: Object

        Returns:
            object: Stats or Exit
        """
        menu = get_menu()

        if menu.play:
            ready = player.is_ready()
            if not ready:
                return self.do_menu(self)

            user.name = player.get_name()
            engine.run(
                MODULES[game.get_game()],
                user=user,
            )

        elif menu.stats:
            return self.do_stats(self)

        elif menu.exit:
            return self.do_exit(self)

    @staticmethod
    def do_stats(line=None):
        """Stats           -- show statistics.

        Args:
            line: pass
        """

        @db_session
        def show_data():
            persons = select(p for p in Players)
            persons.show()
        show_data()
        # print("  Player:", user.name)
        # print(
        #     "  Score :",
        #     user.score,
        #     NEWLINE,
        # )

    @staticmethod
    def do_exit(line=None):
        """Exit           -- finish the game.

        Args:
            line: Pass

        Returns:
            bool: Bool true.
        """
        return True


if __name__ == "__main__":
    print("Welcome to the OASIS!", "\n")

    try:
        GameShell().cmdloop()
    except Exception:
        print("Oops, everything seems to have fallen")

    print("Thanks for Playing!")
