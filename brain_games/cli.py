"""Greeting messages and users representation."""

import prompt


def greet():
    """General user greeting."""
    return 'Welcome to the Brain Games!'


def get_player_name():
    """Getting the user name."""
    user_name = prompt.string('May I have your name? ')
    return user_name


def player_greet(name):
    """Player user greeting."""
    return 'Hello, {player}!'.format(player=name)