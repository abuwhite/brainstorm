# -*- coding: utf-8 -*-

"""Module with the logic of the game calc."""

import random

NAME = "Calc"
RULES = "What is the result of the expression?"


def calculate_expression(first_num, second_num, operator):
    """Вычисляем выражение.

    Args:
        first_num (int): Первое число.
        second_num (int): Второе число.
        operator (str): Оператор.

    Returns:
        str: Возвращаем выражение, которые было образовано от оператора.
    """
    return {
        "+": lambda: str(first_num + second_num),
        "-": lambda: str(first_num - second_num),
        "*": lambda: str(first_num * second_num),
    }.get(operator, lambda: "Not a valid operation")()


def generate_question():
    """Generate first, second number and operator.

    Returns:
        tuple: Number, Operator, Number
    """
    first_num = random.randint(1, 10)
    second_num = random.randint(1, 10)
    operator = random.choice("+-*")
    if first_num <= second_num:
        return second_num, operator, first_num
    return first_num, operator, second_num


# Генерируем вопрос и правильный ответ
def generate_round():
    """Генерируем раунд.

    Returns:
        tuple: Возвращаем вопрос и правильный ответ на вопрос.

    """
    first, op, second = generate_question()
    question = "{num_1} {op} {num_2}".format(num_1=first, num_2=second, op=op)
    answer = calculate_expression(first, second, op)
    return question, answer
