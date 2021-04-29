"""The main client module of the game gcd."""

from brain_games import games
from brain_games.scripts import engine


def main():
    """Скрипт запуска движка с логикой игры."""
    engine.run(games.gcd)


if __name__ == '__main__':
    main()
