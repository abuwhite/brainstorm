"""Cli module."""

from brainstorm.db.schema import add_data


class User(object):
    """Users data: name and score."""

    def __init__(self, name=None, score=0):
        """Player name and score.

        Args:
            name: Player name (str)
            score: Player score (int)
        """
        self._name = name
        self._score = score

    @property
    def name(self):
        """Return player's name.

        Returns:
            str: Player's name.
        """
        return self._name

    @name.setter
    def name(self, new_name):
        if self._name is None or self._name == new_name:
            self._name = new_name
        else:
            self._name = new_name
            self._score = 0
            add_data(new_name, 0)

    @property
    def score(self):
        """Return player's score.

        Returns:
            int: Player's score.
        """
        return self._score

    @score.setter
    def score(self, new_score):
        add_data(self._name, new_score)


user = User()
