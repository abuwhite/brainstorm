"""Greeting messages and users representation."""

import prompt


def greet():
    """Приветствуем пользователя в игре.

    Returns:
        str: Приветствие пользователя в игре.
    """
    return 'Welcome to the Brain Games!'


def get_player_name():
    """Запрос имени пользователя.

    Returns:
        str: Возвращаем имя игрока.
    """
    return prompt.string('May I have your name? ')


def player_greet(name):
    """Приветствие игрока.

    Args:
        name: Имя игрока

    Returns:
        str: Приветствуем игрока по имени.
    """
    return 'Hello, {player}!'.format(player=name)
