# -*- coding: utf-8 -*-

"""Game engine module."""

import prompt
from oasis.config import NUMBER_ROUNDS


def run(game, player_name):
    """Start engine game."""
    print(game.RULES)

    round_count = 0  # Счётчик раундов
    while round_count < NUMBER_ROUNDS:
        question, correct = game.generate_round()

        # Задаём вопрос игроку
        print('Question: {random}'.format(random=question))

        # Получаем ответ игрока
        answer = prompt.string('Your answer: ')

        # Если игрок даст не верный ответ завершаем игру и выводим сообщение
        if answer != correct:
            first = "'{a}' is wrong answer ;(.".format(a=answer)
            second = "Correct answer was '{b}'".format(b=correct)
            print(first, second)
            print("Let's try again, {user}!".format(user=player_name))
            break
        print('Correct!')  # Выводим сообщение
        round_count += 1  # Увеличиваем счётчик
    else:
        # Поздравляем игрока и завершаем игру
        print('Congratulations, {user}!'.format(user=player_name))
