from oasis.__main__ import GameShell
from oasis.utils.menu import MainMenu

def test_stats(capsys):
    text = """  Player: None
  Score : 0 

"""

    GameShell.do_stats()
    captured = capsys.readouterr()
    assert captured.out == text


def test_exit():
    actual = GameShell.do_exit()
    assert actual is True


def test_default(capsys):
    text = """I do not understand that command.
Type help or ? to list commands.

"""
    GameShell.default(..., ...)
    captured = capsys.readouterr()
    assert captured.out == text
