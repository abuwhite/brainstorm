# -*- coding: utf-8 -*-

"""Game engine module."""

import prompt
from oasis.config.config import NUMBER_ROUNDS
from termcolor import colored, cprint


def run(game, player_name):
    """Start engine game."""
    print(game.RULES, '\n')

    score = 0
    round_count = 0  # Rounds counter
    while round_count < NUMBER_ROUNDS:
        question, correct = game.generate_round()

        # Ask player
        print('Question: {random}'.format(random=question))

        # Receive player answer
        answer = prompt.string('Your answer: ')

        if answer != correct:
            first = "'{a}' is wrong answer ;(.".format(a=answer)
            second = "Correct answer was '{b}'".format(b=correct)
            print(colored(first, 'red'), colored(second, 'green'))
            print("Let's try again, {user}!\n".format(user=player_name))
            break

        cprint('Correct!', 'green')
        round_count += 1
        score += 1

    else:
        cprint('Congratulations, {user}!\n'.format(user=player_name),
               'magenta',
               attrs=['bold']
               )

    return score
