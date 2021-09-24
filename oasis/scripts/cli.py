# -*- coding: utf-8 -*-

"""Greeting messages and users representation."""


class Player:
    def __init__(self, name=None, game=None):
        self._name = name

        # if game.startswith('0'):
        #     self._game = game

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def game(self):
        return self._game
