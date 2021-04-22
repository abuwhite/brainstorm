"""Main cli module for calc game."""

import prompt
import random
from brain_games.scripts.brain_games import greeting, user_greeting
from brain_games.cli import get_name


def main():
    greeting()
    user_name = get_name()
    welcome_user = user_greeting(user_name)
    print(welcome_user)
    print(user_name)


if __name__ == '__main__':
    main()