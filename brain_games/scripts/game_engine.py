#!/usr/bin/env python

"""Игровой движок."""

import prompt
from brain_games.cli import greet, get_player_name, player_greet


NUMBER_ROUNDS = 3  # количество раундов в игре.


def game_engine(game):

    print(greet())  # приветствуем пользователя в игре.

    player_name = get_player_name()  # спрашиваем, как зовут игрока.
    greeting_player = player_greet(player_name)
    print(greeting_player)  # приветствуем игрока по имени.

    condition_game = game('condition')
    print(condition_game)  # показываем условия игры.

    round_count = 0  # счётчик раундов, начинаем с 0.
    while round_count < NUMBER_ROUNDS:
        (question, game_answer) = game()
        print('Question: {random}'.format(random=question))

        player_answer = prompt.string('Your answer: ')
        if player_answer == game_answer:
            print('Correct!')
            round_count += 1
            continue

        wrong = "'{wrong}' is wrong answer ;(. ".format(wrong=player_answer)
        correct = "Correct answer was '{correct}'".format(correct=game_answer)

        print(wrong + correct)
        return print("Let's try again, {user}!".format(user=player_name))

    return print('Congratulations, {user}!'.format(user=player_name))
