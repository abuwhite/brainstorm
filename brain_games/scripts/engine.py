#!/usr/bin/env python

"""Игровой движок."""

import prompt
from brain_games import cli

NUMBER_ROUNDS = 3  # Количество раундов в игре.


def run(game):
    """Приветствует игрока, показывает правила и запускает игру."""

    # Приветствуем пользователя в игре
    initial_greeting = cli.greet()
    print(initial_greeting)

    # Спрашиваем имя игрока у пользователя
    player_name = cli.get_player_name()

    # Приветствуем игрока по имени
    greeting_player = cli.player_greet(player_name)
    print(greeting_player)

    # Рассказываем о правилах игры
    print(game.RULES)

    round_count = 0  # Счётчик раундов
    while round_count < NUMBER_ROUNDS:
        (question, answer) = game.generate_round()

        # Задаём вопрос игроку
        print('Question: {random}'.format(random=question))

        # Получаем ответ игрока
        player_answer = prompt.string('Your answer: ')

        # Если игрок даст верный ответ
        if player_answer == answer:
            print('Correct!')  # Выводим сообщение
            round_count += 1  # Увеличиваем счётчик
            continue  # Повторяем цикл

        wrong = "'{wrong}' is wrong answer ;(.".format(wrong=player_answer)
        correct = "Correct answer was '{correct}'".format(correct=answer)
        end_game = "Let's try again, {user}!".format(user=player_name)

        # Если игрок даст неверный ответ, завершаем игру и выводим сообщение
        print(wrong, correct)
        print(end_game)
        return

        # Если игрок ответил на все верно, поздравляем игрока и завершаем игру
    return print('Congratulations, {user}!'.format(user=player_name))
