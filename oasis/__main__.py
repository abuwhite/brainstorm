# -*- coding: utf-8 -*-

"""Игровой движок."""

import prompt
from oasis.scripts.cli import Player
from oasis.scripts import engine
from oasis.config import GAMES, MODULES

user = Player()


def run():
    """
    Greets the player, shows the rules and starts the game.
    """

    # Приветствуем пользователя в игре
    print('Добро пожаловать в Winsio!')

    # Спрашиваем имя у пользователя и запоминаем
    user.name = prompt.string('Как вас зовут? ')

    print('Привет, {user}, выбери игру:'.format(user=user.name))
    print()
    print('\n'.join(GAMES))
    game_index = prompt.integer('Введите цифру: ', 0)
    print()

    print('[START GAME]', MODULES[game_index].NAME)

    engine.run(MODULES[game_index], player_name=user.name)


if __name__ == '__main__':
    run()
