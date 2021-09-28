from oasis.__main__ import create_title, main


def test_create_title():
    actual = create_title('Hello')
    assert actual == print('============= [Hello] =============')
