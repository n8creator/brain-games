#!/usr/bin/env python3
"""Brain Calc call script."""

from brain_games.engine import play_game
from brain_games.games import calc


def main():
    """ Start Brain Progression game."""
    play_game(calc)


if __name__ == '__main__':
    main()
