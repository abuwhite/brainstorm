"""The main client module of the game progression."""

from brain_games import games, engine


def main():
    """Скрипт запуска движка с логикой игры."""
    engine.run(games.progression)


if __name__ == '__main__':
    main()
