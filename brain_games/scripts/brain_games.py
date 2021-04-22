#!/usr/bin/env python

"""Greeting messages and users representation."""

from brain_games import cli


def greeting():
    """Make a user interface."""
    print('Welcome to the Brain Games!')


def user_greeting(user_name):
    """Make a user interface."""
    return print('Hello, {user}!'.format(user=user_name))


def main():
    greeting()


if __name__ == '__main__':
    main()
