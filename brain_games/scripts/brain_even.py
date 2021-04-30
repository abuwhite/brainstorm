#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The main client module of the game even."""

from brain_games import engine, games


def main():
    """Скрипт запуска движка с логикой игры."""
    engine.run(games.even)


if __name__ == '__main__':
    main()
