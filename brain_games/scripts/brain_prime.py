"""The main client module of the game prime."""

from brain_games import games
from brain_games.scripts import engine


def main():
    """Скрипт запуска движка с логикой игры."""
    engine.run(games.prime)


if __name__ == '__main__':
    main()
