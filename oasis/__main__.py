# -*- coding: utf-8 -*-

"""Main module."""

import cmd

from oasis.config import MODULES, NEWLINE
from oasis.scripts import engine
from oasis.scripts.cli import user
from oasis.utils import game, player
from oasis.utils.menu import get_menu
from termcolor import colored


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
    def do_stats(line):
        """Stats           -- show statistics.

        Args:
            line: pass
        """
        print(colored("  Player:", attrs=["bold"]), user.name)
        print(
            colored("  Score :", attrs=["bold"]),
            user.score,
            NEWLINE,
        )

    @staticmethod
    def do_exit(line):
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
