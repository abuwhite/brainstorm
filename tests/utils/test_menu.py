from brainstorm.utils.menu import MainMenu, get_menu


def test_main_menu():
    menu = MainMenu({'menu': 'play'})
    assert menu.play is True
    assert menu.stats is False
