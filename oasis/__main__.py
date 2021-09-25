# -*- coding: utf-8 -*-

"""Игровой движок."""
import cmd
import time
import prompt
from oasis.config import GAMES, MODULES
from oasis.scripts import engine
from oasis.scripts.cli import Player

user = Player()


def run():
    """Greets the player, shows the rules and starts the game."""

    # Player great
    time.sleep(1.6)
    print()

    # Ask user name
    print("What's your name?")
    user.name = prompt.string('\n> ')

    time.sleep(1.6)
    print('Hey, {user}, choose game:'.format(user=user.name))

    time.sleep(1)
    print()
    print('\n'.join(GAMES) + '\n')
    game_index = prompt.integer('Enter number: ', 0)
    print()

    time.sleep(1.8)
    print('[START GAME]', MODULES[game_index].NAME)

    engine.run(MODULES[game_index], player_name=user.name)


class GameShell(cmd.Cmd):
    intro = 'Welcome to the Winsio.   Type help or ? to list commands.\n'
    prompt = '> '

    # The default() method is called when none of the other do_*() command methods match.
    def default(self, line):
        print('I do not understand that command. Type help or ? to list commands.\n')

    def do_start(self, line):
        """start           -- Initializing the game engine"""
        run()

    # A very simple "quit" command to terminate the program:
    def do_quit(self, line):
        return True  # this exits the Cmd application loop in TextAdventureCmd.cmdloop()

    def help_combat(self):
        print('Combat is not implemented in this program.')

    def help_game(self):
        print('Help for this game.')


if __name__ == '__main__':
    # print('Text Adventure Demo!')
    # print('====================')

    GameShell().cmdloop()
    print('Thanks for playing!')
