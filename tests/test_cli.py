"""Cli module."""

from brainstorm.scripts.cli import User


def test_init_player():
    user = User()
    name = user.name
    score = user.score

    assert name is None
    assert score == 0


def test_new_score_player():
    user = User()
    user.score = 10
    assert user.score == 10


def test_new_player():
    user = User("Mark", 5)
    user.name = "Anna"
    assert user.score == 0
