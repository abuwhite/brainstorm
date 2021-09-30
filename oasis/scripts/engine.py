# -*- coding: utf-8 -*-

"""Game engine module."""

import prompt
from oasis.config.config import NUMBER_ROUNDS
from termcolor import colored, cprint


def player_ready():
    answer = prompt.string("Are you ready? (y/n): ")
    return True if answer == 'y' else False


def run(game, player_name):
    """Start engine game.

    Args:
        game: Game module.
        player_name: Player's name.

    Returns:
        int: Player score.
    """
    print(game.RULES, "\n")

    ready = player_ready()
    if ready:
        score = 0
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
            score += 1

        else:
            cprint(
                "Congratulations, {user}!\n".format(user=player_name),
                "magenta",
                attrs=["bold"],
            )

        return score
