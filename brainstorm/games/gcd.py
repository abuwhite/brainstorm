# -*- coding: utf-8 -*-

"""Module with the logic of the game gcd."""
import math
import random

NAME = "GCD"
RULES = "Find the greatest common divisor of given numbers."


def generate_question():
    """Генерируем первое и второе число от 1 до 100.

    Returns:
        int: Возращаем первое случайно сгенерированное число.
        int: Возращаем второе случайно сгенерированное число.

    """
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    return first_num, second_num


def generate_round():
    """
    Генерируем раунд.

    Returns:
        str: question Вопрос пользователю
        str: result Правильный ответ на вопрос
    """
    first_num, second_num = generate_question()
    question = "{one} {two}".format(one=first_num, two=second_num)
    answer = str(math.gcd(first_num, second_num))
    return question, answer
