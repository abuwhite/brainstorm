"""The main client module of the game even."""

from brain_games import engine, games


def main():
    engine.run(games.calc)


if __name__ == '__main__':
    main()
