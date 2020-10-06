#!/usr/bin/env python3
"""Brain GCD call script."""

from brain_games.engine import play_game
from brain_games.games import gcd


def main():
    """ Start Brain GCD game."""
    play_game(gcd)


if __name__ == '__main__':
    main()
