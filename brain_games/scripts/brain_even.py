#!/usr/bin/env python3
"""Brain Even call script."""

from brain_games.engine import play_game
from brain_games.games import even


def main():
    """ Start Brain Even game."""
    play_game(even)


if __name__ == '__main__':
    main()
