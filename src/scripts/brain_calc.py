#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The main client module of the game calc."""

from src import engine, games


def main():
    """Скрипт запуска движка с логикой игры."""
    engine.run(games.calc)


if __name__ == '__main__':
    main()
