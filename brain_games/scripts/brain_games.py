#!/usr/bin/env python3
"""Brain Games template"""

from brain_games.engine import greeting, get_username


def main():
    """Welcome user and return his name."""
    greeting()
    get_username()


if __name__ == '__main__':
    main()
