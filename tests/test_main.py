from brainstorm.__main__ import main, get_stats, get_out
from brainstorm.utils.menu import MainMenu


def test_stats(capsys):
    text = """  Player: None
  Score : 0 

"""

    get_stats()
    captured = capsys.readouterr()
    assert captured.out == text


def test_exit():
    actual = get_out()
    assert actual is True

