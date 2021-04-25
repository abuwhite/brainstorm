"""The main client module of the game even."""

from brain_games.scripts.game_engine import game_engine
from brain_games.games.even import generate_round


def main():
    game_engine(generate_round)


if __name__ == '__main__':
    main()