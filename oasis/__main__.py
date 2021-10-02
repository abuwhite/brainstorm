# -*- coding: utf-8 -*-

"""Main module."""
from __future__ import print_function, unicode_literals

import cmd

import prompt as pmt
from oasis.config.config import MODULES, ASK_NAME, LIST_GAMES, MENU
from oasis.config.constants import NEWLINE
from oasis.scripts import engine
from oasis.scripts.cli import Player
from termcolor import colored

from PyInquirer import prompt
from pprint import pprint
from examples import custom_style_1, custom_style_2, custom_style_3

user = Player()


def get_user_name(params):
    """Ask for the player's name.

    Set name at user.name
    """
    name = prompt(params, style=custom_style_2)
    user.name = name.get('player')


def get_game(list_games):
    game = prompt(list_games, style=custom_style_3)
    return game.get('game')


def create_title(self):
    """Create title.

    Args:
        self: Other string data.
    """
    print("============= [{title}] =============".format(title=self))


class MainMenu:
    def __init__(self, answer):
        self._play = None
        self._help = None
        self._exit = None

        item = answer.get('menu')
        if item == 'play':
            self._play = True
        elif item == 'help':
            self._help = True
        elif item == 'exit':
            self._exit = True

    @property
    def play(self):
        return self._play

    @play.setter
    def play(self, value=True):
        self._play = value

    @property
    def help(self):
        return self._help

    @help.setter
    def help(self, value=True):
        self._help = value

    @property
    def exit(self):
        return self._exit

    @exit.setter
    def exit(self, value=True):
        self._exit = value


class GameShell(cmd.Cmd):
    """Main game logic."""

    intro = "Press [ENTER] when ready.\n"
    # intro = "Type help or ? to list commands.\n"

    def emptyline(self):
        if self.prompt:
            return self.do_start(self)

    prompt = '> '

    def default(self, line):
        """Get default method.

        Args:
            line: Default line.
        """
        print("I do not understand that command.")
        print("Type help or ? to list commands.\n")

    @staticmethod
    def do_start(self):
        answer = prompt(MENU, style=custom_style_1)
        menu = MainMenu(answer)

        if menu.play:
            game = get_game(LIST_GAMES)
            # create_title(MODULES[game].NAME)

            def player_ready():
                """Check player ready.

                Returns:
                    bool: True if Player ready else False
                """
                questions = [
                    {
                        'type': 'confirm',
                        'message': 'Do you want to continue?',
                        'name': 'continue',
                        'default': True,
                    },
                ]
                ready = prompt(questions, style=custom_style_1)
                if ready.get('continue'):
                    return True
            ready = player_ready()
            if not ready:
                return self.do_start(self)

            engine.run(MODULES[game], player_name=user.name, user=user)

        elif menu.help:
            pass
        elif menu.exit:
            return True

    @staticmethod
    def do_stats(line):
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

    @staticmethod
    def do_quit(line):
        """Quit           -- finish the game.

        Args:
            line: Pass

        Returns:
            bool: Bool true.
        """
        return True


if __name__ == "__main__":
    print('Welcome to the OASIS!', '\n')

    # get_user_name(ASK_NAME)

    GameShell().cmdloop()
    # try:
    #     GameShell().cmdloop()
    # except Exception:
    #     print("Oops, everything seems to have fallen")

    print("Thanks for playing!")
