# -*- coding: utf-8 -*-

"""Main module."""

import cmd
import textwrap as tw
import prompt
from termcolor import colored
from oasis.config.config import GAMES, MODULES
from oasis.scripts import engine
from oasis.scripts.cli import Player


user = Player()

NEWLINE = '\n'


def create_title(data):
    print('============= [{}] ============='.format(data))


def main():
    """Greets the player, shows the rules and starts the game."""

    print("{n}What's your name?".format(n=NEWLINE))
    user.name = prompt.string('> ')

    print('{n}Hey, {user}, choose game:'.format(n=NEWLINE, user=user.name))

    print('    '.join(GAMES), NEWLINE)
    game_index = prompt.integer('Enter number: ', 0)
    print()

    create_title(MODULES[game_index].NAME)

    user.score = engine.run(MODULES[game_index], player_name=user.name)


class GameShell(cmd.Cmd):
    intro = 'Welcome to the OASIS.   Type help or ? to list commands.\n'
    prompt = '> '

    def default(self, line):
        print('I do not understand that command. Type help or ? to list commands.\n')

    @staticmethod
    def do_start(line):
        """start           -- start the game"""
        main()

    @staticmethod
    def do_stats(line):
        """stats           -- show statistics"""
        create_title('STATS')
        print(colored('Player:', attrs=['bold']), user.name)
        print(colored('Score:', attrs=['bold']),
              user.score,
              NEWLINE
              )

    @staticmethod
    def do_quit(line):
        """quit           -- finish the game"""
        return True

    @staticmethod
    def help_game():
        description = """
        A set of five console games along the lines of popular mobile brain-pumping apps. 
        Each game asks questions that need to be answered correctly.
        After three correct answers, the game is considered completed.
        Incorrect answers end the game and prompt you to play it again.
        """
        dedented_text = tw.dedent(description).strip()
        print(NEWLINE, tw.fill(dedented_text, width=50), NEWLINE)


if __name__ == '__main__':
    try:
        GameShell().cmdloop()
    except Exception:
        print('Oops, everything seems to have fallen')

    print('Thanks for playing!')
