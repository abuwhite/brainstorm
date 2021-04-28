"""Module with the logic of the game even."""

import random


def calculate_expression(first_num, second_num, operator):
    if operator == '+':
        return str(first_num + second_num)
    if operator == '-':
        return str(abs(first_num - second_num))
    if operator == '*':
        return str(first_num * second_num)


def generate_question():
    first_num = random.randint(1, 10)
    second_num = random.randint(1, 10)
    operator = random.choice('+-*')
    return first_num, operator, second_num


# Правила игры
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


# Генерируем вопрос и правильный ответ
def generate_round():
    (num_1, op, num_2) = generate_question()
    question = '{num_1} {op} {num_2}'.format(num_1=num_1, num_2=num_2, op=op)
    answer = calculate_expression(num_1, num_2, op)
    return question, answer
