# -*- coding: utf-8 -*-

"""Игровой движок."""

import prompt
from oasis.cli import Player

NUMBER_ROUNDS = 3  # Количество раундов в игре.

user = Player()

def start():
    """
    Приветствует игрока, показывает правила и запускает игру.

    Args:
        game: Логика игры
    """
    # Приветствуем пользователя в игре
    print('Welcome to the Winsio!')

    # Спрашиваем имя игрока у пользователя, и запоминаем
    user.name = prompt.string('May I have your name? ')

    # Приветствуем игрока по имени
    print(user.greet)


if __name__ == '__main__':
    start()