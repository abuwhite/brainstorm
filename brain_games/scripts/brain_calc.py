#!/usr/bin/env python

"""The main client module of the game calc."""

from brain_games import engine, games


def main():
    """Скрипт запуска движка с логикой игры."""
    engine.run(games.calc)


if __name__ == '__main__':
    main()
