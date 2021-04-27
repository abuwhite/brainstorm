"""Module with the logic of the game even."""

import random


def generate_correct_answer(first, second, operator):
    if operator == '+':
        return str(first + second)
    if operator == '-':
        return str(first - second)
    if operator == '*':
        return str(first * second)


def generate_operator():
    operators = '+-*'
    return random.choice(operators)


def generate_number():
    return random.randint(1, 10)


def generate_question():
    first_num = generate_number()
    second_num = generate_number()
    operator = generate_operator()
    return first_num, second_num, operator


def generate_round(condition=False):
    if condition == 'condition':
        return 'What is the result of the expression?'
    (first, second, op) = generate_question()
    question = '{one} {op} {two}'.format(one=first, two=second, op=op)
    answer = generate_correct_answer(first, second, op)
    return question, answer
