# -*- coding: utf-8 -*-

"""Game engine module."""
from brainstorm.config import BOLD, NUMBER_ROUNDS
from brainstorm.utils.colors import style2
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
            "message": "Question: {ask}".format(ask=text),
        },
    ]

    return prompt(question, style=style2).get("answer")


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
            cprint("Correct!", "green")
            round_count += 1
            user.score += 1
            continue

        print(
            colored(
                "{a}".format(a=answer),
                color="red",
                attrs=[BOLD],
            ),
            "is wrong answer.",
        )

        print(
            "Correct answer was",
            colored(
                "{b}".format(b=correct),
                color="green",
                attrs=[BOLD],
            ),
        )

        cprint(
            "Let's try again, {name}!\n".format(name=user.name),
            color="yellow",
            attrs=[BOLD],
        )

        break

    else:
        cprint(
            "Congratulations, {name}!\n".format(name=user.name),
            color="magenta",
            attrs=[BOLD],
        )
