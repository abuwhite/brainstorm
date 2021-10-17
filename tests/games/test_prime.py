from brainstorm.games import prime


def test_is_prime():
    actual = prime.is_prime(4)
    assert actual == "no"

    actual = prime.is_prime(3)
    assert actual == "yes"


def test_is_prime_type():
    actual = prime.is_prime(8)
    assert isinstance(actual, str)


def test_generate_number_type():
    actual = prime.generate_number()
    assert isinstance(actual, int)


def test_generate_round():
    actual = prime.generate_round()
    assert isinstance(actual, tuple)
    assert isinstance(actual[0], int)
    assert isinstance(actual[1], str)
