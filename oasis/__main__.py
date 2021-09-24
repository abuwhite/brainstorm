# -*- coding: utf-8 -*-

"""Игровой движок."""

import prompt
from oasis.scripts.cli import Player
from oasis.scripts import engine
from oasis.games import calc
from oasis import config

user = Player()


def run():
    """
    Greets the player, shows the rules and starts the game.
    """

    # Приветствуем пользователя в игре
    print('Welcome to the Winsio!')

    # Спрашиваем имя у пользователя и запоминаем
    user.name = prompt.string('May I have your name? ')

    text = 'Hello, {user}, choose a game:'.format(user=user.name) + '\n' + '\n'.join(config.GAMES)

    print(text)

    engine.run(calc, player_name=user.name)


if __name__ == '__main__':
    run()
