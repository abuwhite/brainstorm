"""Main cli module for even game."""

import prompt
import random
from brain_games.scripts.brain_games import greeting, user_greeting
from brain_games.cli import get_name


def is_even(num):
    if (num % 2) == 0:
        return 'yes'
    return 'no'


def even(name):
    counter = 0
    round_count = 3
    while counter < round_count:
        question = random.randint(1, 10)
        print('Question: {random}'.format(random=question))

        user_answer = prompt.string('Your answer: ')
        correct_answer = is_even(question)

        if user_answer != correct_answer:
            return print('\'{wrong}\' is wrong answer ;(. Correct answer was \'{correct}\'. '
                         '\nLet\'s try again, {user}!'.format(wrong=user_answer,
                                                              correct=correct_answer,
                                                              user=name))

        print('Correct!')
        counter += 1

    print('Congratulations, {user}!'.format(user=name))


def main():
    greeting()
    user_name = get_name()

    print(user_greeting(user_name))
    print('Answer "yes" if the number is even, otherwise answer "no".')

    even(user_name)


if __name__ == '__main__':
    main()
