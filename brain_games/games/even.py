"""Module with the logic of the game even."""

import random


def is_even(num):
    return True if (num % 2) == 0 else False


def get_answer(question):
    return 'yes' if is_even(question) else 'no'


def generate_number():
    return random.randint(1, 10)


# Правила игры
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


# Генерируем вопрос и правильный ответ
def generate_round():
    question = generate_number()
    answer = get_answer(question)
    return question, answer
