#!/usr/bin/env python

"""Greeting messages and users representation."""

from brain_games import cli


def greeting():
    """General user greeting."""
    print('Welcome to the Brain Games!')


def user_greeting(user_name):
    """Player's greeting."""
    return 'Hello, {user}!'.format(user=user_name)


def main():
    greeting()


if __name__ == '__main__':
    main()
