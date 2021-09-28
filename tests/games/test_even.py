from oasis.games import even


def test_is_even():
    actual = even.is_even(2)
    assert actual == "yes"

    actual = even.is_even(3)
    assert actual == "no"


def test_generate_number_type():
    actual = even.generate_number()
    assert isinstance(actual, int)


def test_generate_round_type():
    actual = even.generate_round()
    assert isinstance(actual, tuple)
