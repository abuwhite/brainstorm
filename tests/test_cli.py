"""Cli module."""

from oasis.scripts.cli import Player


def test_init_player():
    user = Player()
    name = user.name
    score = user.score

    assert name is None
    assert score == 0


def test_new_score_player():
    user = Player()
    user.score = 10
    assert user.score == 10


def test_new_player():
    user = Player("Mark", 5)
    user.name = "Anna"
    assert user.score == 0
