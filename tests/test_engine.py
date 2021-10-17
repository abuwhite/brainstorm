import unittest.mock as mock
import pytest

from brainstorm.scripts import engine
from brainstorm.games import calc


# def test_player_ready(monkeypatch):
#     with monkeypatch.context() as m:
#         m.setattr('builtins.input', lambda prompt="": "y")
#         result = engine.player_ready()
#     assert result is True
