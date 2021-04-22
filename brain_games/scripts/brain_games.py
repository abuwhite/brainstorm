#!/usr/bin/env python

"""Greeting messages and users representation."""

from brain_games import cli


def greeting(user_name):
    """General user greeting."""
    if user_name:
        return 'Hello, {user}!'.format(user=user_name)
    print('Welcome to the Brain Games!')


def main():
    greeting()


if __name__ == '__main__':
    main()
