# -*- coding: utf-8 -*-

"""Module with the logic of the game prime."""

import random

NAME = "Prime"
RULES = '"yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """Check whether the number is prime or not.

    Args:
        num: Random number from 1 to 10

    Returns:
        str: If the number is prime, then we return yes, otherwise no.
    """
    if num > 1:
        # check for factors
        for index in range(2, num):
            if (num % index) == 0:
                return "no"
        return "yes"
    return "no"


def generate_number() -> int:
    """Generate a random number from 1 to 10.

    Returns:
        int: Random number.
    """
    return random.randint(1, 10)


def generate_round() -> tuple:
    """
    Generate round.

    Returns:
        tuple: Question, Correct Answer
    """
    question = generate_number()
    answer = is_prime(question)
    return question, answer
