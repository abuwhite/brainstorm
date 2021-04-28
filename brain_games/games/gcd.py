"""Module with the logic of the game gcd."""


# Правила игры
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    """
    Генерируем раунд.

    Returns:
        question: Вопрос пользователю
        result: Правильный ответ на вопрос
    """
    question = generate_number()
    answer = get_correct_result(question)
    return question, answer