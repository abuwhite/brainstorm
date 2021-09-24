# -*- coding: utf-8 -*-

"""Module with the logic of the game prime."""

import random

NAME = 'Prime'
RULES = '"yes" if given number is prime. Otherwise answer "no".'


def get_correct_result(num):
    """Проверяем, является ли число простым или нет.

    Args:
        num (int): Случайное число от 1 до 10

    Returns:
        bool: Если число простое, то возвращаем да, иначе нет.
    """
    if num > 1:
        # check for factors
        for index in range(2, num):
            if (num % index) == 0:
                return 'no'
        return 'yes'
    return 'no'


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
    answer = get_correct_result(question)
    return question, answer
