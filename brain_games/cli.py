"""This is an cli."""
import prompt


def welcome_user():
    """Return user name.

    # noqa: DAR201

    """
    user_name = prompt.string('May I have your name? ')
    return 'Hello, {user}!'.format(user=user_name)
