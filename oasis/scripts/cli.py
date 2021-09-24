# -*- coding: utf-8 -*-

"""Greeting messages and users representation."""


class Player:
    def __init__(self, name=None):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
