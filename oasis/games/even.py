# -*- coding: utf-8 -*-

"""Module with the logic of the game even."""

import random

NAME = "Even"
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """Проверяем, является ли число простым или нет.

    Args:
        num (int): Случайное число от 1 до 10

    Returns:
        bool: Если число простое, то возвращаем да, иначе нет.
    """
    return "yes" if (num % 2) == 0 else "no"


def generate_number():
    """Генерируем случайное число от 1 до 10.

    Returns:
        int: Возвращаем случайное число.
    """
    return random.randint(1, 10)


def generate_round():
    """
    Генерируем раунд.

    Returns:
        question: Вопрос пользователю
        result: Правильный ответ на вопрос
    """
    question = generate_number()
    answer = is_even(question)
    return question, answer
