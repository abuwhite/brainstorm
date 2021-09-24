# -*- coding: utf-8 -*-

"""Module with the logic of the game gcd."""
import random

# Правила игры
RULES = 'What number is missing in the progression?'

# Длина прогрессии
PROGRESSION_LENGTH = 10


def generate_numbers():
    """
    Генерируем цифры.

    Returns:
        question: Вопрос пользователю
        result: Правильный ответ на вопрос
    """
    starting_number = random.randint(1, 10)
    progression_num = random.randint(2, 5)

    total_numbers = starting_number

    index = 0
    while index < PROGRESSION_LENGTH:
        total_numbers += progression_num
        index += 1

    progression = range(starting_number, total_numbers, progression_num)
    random_numbers = random.choice(progression)

    total_num = []

    for number in progression:
        if number == random_numbers:
            total_num.append(str('..'))
            continue
        total_num.append(str(number))
    return total_num, random_numbers


def generate_round():
    """
    Генерируем раунд.

    Returns:
        question: Вопрос пользователю
        result: Правильный ответ на вопрос
    """
    total_num, random_num = generate_numbers()
    question = ' '.join(total_num)
    answer = str(random_num)
    return question, answer
