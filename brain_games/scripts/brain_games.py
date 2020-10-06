#!/usr/bin/env python3
"""Brain Games template script."""

import prompt


def main():
    # Print Welcome message
    print('Welcome to Brain Games!')

    # Ask user for his name and greet him
    name = prompt.string('May I have your name?: ')
    print('Hello, {0}!\n'.format(name))


if __name__ == '__main__':
    main()
