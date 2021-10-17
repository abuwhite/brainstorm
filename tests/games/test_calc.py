from brainstorm.games import calc


def test_calculate_expression():
    actual = calc.calculate_expression(1, 1, "+")
    assert len(actual) == 1


def test_calculate_expression_type():
    actual = calc.calculate_expression(1, 1, "+")
    assert isinstance(actual, str)


def test_calculate_expression_calc():
    actual_add = calc.calculate_expression(4, 4, "+")
    actual_sub = calc.calculate_expression(8, 3, "-")
    actual_mul = calc.calculate_expression(2, 2, "*")
    assert actual_add == "8" and isinstance(actual_add, str)
    assert actual_sub == "5" and isinstance(actual_add, str)
    assert actual_mul == "4" and isinstance(actual_add, str)


def test_generate_question():
    actual = calc.generate_question()
    assert len(actual) == 3


def test_generate_question_type():
    actual = calc.generate_question()
    assert isinstance(actual, tuple)


def test_generate_round():
    actual = calc.generate_round()
    assert len(actual) == 2


def test_generate_round_type():
    actual = calc.generate_round()

    assert isinstance(actual[0], str)
    assert isinstance(actual[1], str)
    assert isinstance(actual, tuple)
