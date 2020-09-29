"""Hexlet 1-st project."""

import prompt


def welcome_user():
    """Ask User name and Greet him."""
    name = prompt.string('May I have your name?: ')
    print('Hello, {0}!\n'.format(name))
