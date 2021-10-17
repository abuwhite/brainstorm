from brainstorm.games import gcd


def test_generate_question():
    actual = gcd.generate_question()
    assert len(actual) == 2


def test_generate_question_type():
    actual = gcd.generate_question()

    assert isinstance(actual[0], int)
    assert isinstance(actual[1], int)
    assert isinstance(actual, tuple)


def test_generate_round():
    actual = gcd.generate_round()
    assert len(actual) == 2


def test_generate_round_type():
    actual = gcd.generate_round()
    assert isinstance(actual[0], str)
    assert isinstance(actual[1], str)
