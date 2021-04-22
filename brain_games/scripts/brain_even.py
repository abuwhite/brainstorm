
"""Main cli module for even game."""

import prompt
from random import randint


def is_even(num):
    if (num % 2) == 0:
        return 'yes'
    return 'no'


def main():
    print('Welcome to the Brain Games!\n')

    user_name = prompt.string('May I have your name? ')
    print('Hello, {user}!'.format(user=user_name))

    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0
    round_count = 3
    while counter < round_count:
        question = randint(1, 10)
        print('Question: {random}'.format(random=question))

        user_answer = prompt.string('Your answer: ')
        correct_answer = is_even(question)

        if user_answer != correct_answer:
            return print('\'{wrong}\' is wrong answer ;(. Correct answer was \'{correct}\'. '
                         '\nLet\'s try again, {name}!'.format(wrong=user_answer,
                                                             correct=correct_answer,
                                                             name=user_name))

        print('Correct!')
        counter += 1

    print('Congratulations, {name}!'.format(name=user_name))


if __name__ == '__main__':
    main()