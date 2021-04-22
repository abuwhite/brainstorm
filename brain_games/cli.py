"""This is an cli."""

import prompt

def get_name():
    """Make a user interface."""
    user_name = prompt.string('May I have your name? ')
    return user_name

def main():
    get_name()


if __name__ == '__main__':
    main()