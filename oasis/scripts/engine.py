# -*- coding: utf-8 -*-

"""Game engine module."""

import prompt
from oasis.config.config import NUMBER_ROUNDS
from termcolor import colored, cprint

"""
* Confirm question example
* run example by typing `python example/confirm.py` in your console
"""
from pprint import pprint

from PyInquirer import prompt as pyprompt

from examples import custom_style_1


def player_ready():
    """Check player ready.

    Returns:
        bool: True if Player ready else False
    """
    questions = [
        {
            'type': 'confirm',
            'message': 'Do you want to continue?',
            'name': 'continue',
            'default': True,
        },
        {
            'type': 'confirm',
            'message': 'Do you want to exit?',
            'name': 'exit',
            'default': False,
        },
    ]
    answers = pyprompt(questions, style=custom_style_1)
    pprint(answers)
    # if answer == 'y':
    #     return True


# def player_ready():
#     """Check player ready.
#
#     Returns:
#         bool: True if Player ready else False
#     """
#     answer = prompt.string("Are you ready? (y/n): ")
#     if answer == 'y':
#         return True


def run(game, player_name, user):
    """Start engine game.

    Args:
        game: Game module.
        player_name: Player's name.
        user: Player user class.

    Returns:
        int: Player score.
    """
    print(game.RULES, "\n")

    ready = player_ready()
    if ready:
        round_count = 0  # Rounds counter
        while round_count < NUMBER_ROUNDS:
            question, correct = game.generate_round()

            # Ask player
            print("Question: {random}".format(random=question))

            # Receive player answer
            answer = prompt.string("Your answer: ")

            if answer != correct:
                first = "'{a}' is wrong answer ;(.".format(a=answer)
                second = "Correct answer was '{b}'".format(b=correct)
                print(colored(first, "red"), colored(second, "green"))
                print("Let's try again, {user}!\n".format(user=player_name))
                break

            cprint("Correct!", "green")
            round_count += 1
            user.score += 1

        else:
            cprint(
                "Congratulations, {user}!\n".format(user=player_name),
                "magenta",
                attrs=["bold"],
            )
        return True
    return False
