"""Module with the logic of the game even."""

import random

# Правила игры
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if (num % 2) == 0:
        return 'yes'
    return 'no'


def generate_number():
    return random.randint(1, 10)


def generate_round():
    question = generate_number()
    answer = is_even(question)
    return question, answer
