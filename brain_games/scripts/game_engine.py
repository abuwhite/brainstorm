#!/usr/bin/env python

"""Greeting messages and users representation."""


import prompt
from brain_games import cli


def generate_round(question):
    counter = 0
    NUMBER_ROUNDS = 3
    while counter < NUMBER_ROUNDS:
        print('Question: {random}'.format(random=question))
        counter += 1


def game_engine(condition, question):
    cli.greeting(user_name=False)
    user_name = cli.get_name()

    print(cli.greeting(user_name))
    print(condition)

    generate_round(question)


def main(condition, question):
    game_engine(condition, question)


if __name__ == '__main__':
    main()
