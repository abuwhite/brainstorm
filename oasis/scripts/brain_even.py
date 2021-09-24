#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The main client module of the game even."""

from oasis import __main__, games


def main():
    """Скрипт запуска движка с логикой игры."""
    __main__.start(games.even)


if __name__ == '__main__':
    main()
