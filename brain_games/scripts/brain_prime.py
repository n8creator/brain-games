#!/usr/bin/env python3
"""Brain Prime call script."""

from brain_games.engine import play_game
from brain_games.games import prime


def main():
    """ Start Brain Prime game."""
    play_game(prime)


if __name__ == '__main__':
    main()
