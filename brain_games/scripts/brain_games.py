#!/usr/bin/env python

"""This is an brain-games."""

from brain_games import cli


def main():
    """Return user name.

    # noqa: DAR201

    """
    print('Welcome to the Brain Games!')
    print(cli.welcome_user())


if __name__ == '__main__':
    main()
