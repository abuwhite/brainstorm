from oasis.games import progression


def test_generate_numbers():
    actual = progression.generate_numbers()
    assert isinstance(actual[0], list)
    assert isinstance(actual[1], int)
    assert isinstance(actual, tuple)
    assert len(actual) == 2


def test_generate_round():
    actual = progression.generate_round()
    assert isinstance(actual[0], str)
    assert isinstance(actual[1], str)
    assert isinstance(actual, tuple)
    assert len(actual) == 2