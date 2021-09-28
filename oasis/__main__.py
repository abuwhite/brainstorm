# -*- coding: utf-8 -*-

"""Main module."""

import cmd
import textwrap as tw

import prompt
from oasis.config.config import GAMES, MODULES
from oasis.config.constants import NEWLINE, TEXT_WIDTH
from oasis.scripts import engine
from oasis.scripts.cli import Player
from termcolor import colored

user = Player()


def create_title(self):
    """Create title.

    Args:
        self: Other string data.
    """
    print("============= [{title}] =============".format(title=self))


def main():
    """Greets the player, shows the rules and starts the game."""
    print("{n}What's your name?".format(n=NEWLINE))
    user.name = prompt.string("> ")

    print("{n}Hey, {user}, choose game:".format(n=NEWLINE, user=user.name))

    print("    ".join(GAMES), NEWLINE)
    game_index = prompt.integer("Enter number: ", 0)
    print()

    create_title(MODULES[game_index].NAME)

    user.score = engine.run(MODULES[game_index], player_name=user.name)


def do_stats() -> None:
    """Stats           -- show statistics.

    Args:
        line: pass
    """
    create_title("STATS")
    print(colored("Player:", attrs=["bold"]), user.name)
    print(
        colored("Score:", attrs=["bold"]),
        user.score,
        NEWLINE,
    )


class GameShell(cmd.Cmd):
    """Main game logic."""

    intro = "Welcome to the OASIS.   Type help or ? to list commands.\n"
    prompt = "> "

    def default(self, line):
        """Get default method.

        Args:
            line: Default line.
        """
        print("I do not understand that command. Type help or ? to list commands.\n")

    @staticmethod
    def do_start(line):
        """Start           -- start the game.

        Args:
            line: pass
        """
        main()

    @staticmethod
    def do_quit(line):
        """Quit           -- finish the game.

        Args:
            line: Pass

        Returns:
            bool: Bool true.
        """
        return True

    # @staticmethod
    # def help_game():
    #     description = """
    #     A set of five console games along the lines of popular
    #     mobile brain-pumping apps. Each game asks questions that need
    #     to be answered correctly. After three correct answers, the game
    #     is considered completed. Incorrect answers end the game and
    #     prompt you to play it again.
    #     """
    #     dedented_text = tw.dedent(description).strip()
    #     print(
    #         NEWLINE,
    #         tw.fill(dedented_text, width=TEXT_WIDTH),
    #         NEWLINE,
    #     )


if __name__ == "__main__":
    try:
        GameShell().cmdloop()
    except Exception:
        print("Oops, everything seems to have fallen")

    print("Thanks for playing!")
