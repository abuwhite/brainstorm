#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The main client module of the game gcd."""

from brain_games import engine, games


def main():
    """Скрипт запуска движка с логикой игры."""
    engine.run(games.gcd)


if __name__ == '__main__':
    main()
