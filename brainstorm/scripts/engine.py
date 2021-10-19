# -*- coding: utf-8 -*-

"""Game engine module."""
from brainstorm.config import BOLD, NUMBER_ROUNDS
from brainstorm.utils.colors import menu
from brainstorm.utils.game import print_title
from PyInquirer import prompt
from termcolor import colored, cprint


def get_answer(text):
    """Get player answer.

    Args:
        text: Question

    Returns:
        str: Player answer
    """
    question = [
        {
            "type": "input",
            "name": "answer",
            "message": "{ask}".format(ask=text),
        },
    ]

    return prompt(question, style=menu).get("answer")


def run(game, user):
    """Start engine game.

    Args:
        game: Game module.
        user: Player user class.

    The game lasts up to 3 rounds.
    Each round adds 1 point to the player.
    """
    print_title(game.RULES)

    round_count = 0  # Rounds counter
    while round_count < NUMBER_ROUNDS:
        question, correct = game.generate_round()
        answer = get_answer(question)

        if answer == correct:
            cprint("Right!", "green")
            # print(
            #     colored(
            #         "+1",
            #         color="green",
            #         attrs=[BOLD],
            #     ),
            #     "point",
            # )
            round_count += 1
            user.score += 1
            continue

        cprint("Wrong!", "red")

        # print(
        #     "Correct answer was",
        #     colored(
        #         "{b}".format(b=correct),
        #         color="green",
        #         attrs=[BOLD],
        #     ),
        # )

        # cprint(
        #     "Let's try again, {name}!\n".format(name=user.name),
        #     color="yellow",
        #     attrs=[BOLD],
        # )

        round_count += 1

    else:
        cprint(
            "Поздравляем, {name}".format(name=user.name),
            color="magenta",
            attrs=[BOLD],
        )
