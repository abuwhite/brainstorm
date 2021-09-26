# -*- coding: utf-8 -*-

"""Player module."""


class Player:
    def __init__(self, name=None, score=0):
        self._name = name
        self._score = score

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if self._name is None or self._name == new_name:
            self._name = new_name
        else:
            self._name = new_name
            self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score += value

    @score.deleter
    def score(self):
        del self._score
