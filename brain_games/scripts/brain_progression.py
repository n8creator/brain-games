#!/usr/bin/env python3
"""Brain Progression call script."""

from brain_games.engine import play_game
from brain_games.games import progression


def main():
    """ Start Brain Progression game."""
    play_game(progression)


if __name__ == '__main__':
    main()
