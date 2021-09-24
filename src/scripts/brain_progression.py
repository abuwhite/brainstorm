#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The main client module of the game progression."""

from src import engine, games


def main():
    """Скрипт запуска движка с логикой игры."""
    engine.run(games.progression)


if __name__ == '__main__':
    main()
