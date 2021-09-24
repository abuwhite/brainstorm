#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Brain games main executable module."""

from oasis import cli


def main():
    """Start game."""
    # Приветствуем пользователя в игре
    cli.greet()

    # Спрашиваем имя игрока у пользователя
    player_name = cli.get_player_name()

    # Приветствуем игрока по имени
    print(cli.player_greet(player_name))


if __name__ == 'main':
    main()
