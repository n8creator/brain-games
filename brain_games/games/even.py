"""Brain Game Even Module."""

from random import randint

GAME_INTRO = 'Answer "yes" if number is Even otherwise answer "no".\n'
MIN_VALUE, MAX_VALUE = 1, 100


def generate_game():
    """Brain Games Even Function.

    Generates some random number and check if this number is even

    Returns:
        tuple: question guessed to the user and correct answer
    """

    # Generate ranom number
    question = randint(MIN_VALUE, MAX_VALUE)

    # Calculate correct answer
    correct_answer = 'yes' if (question % 2) == 0 else 'no'

    # Return function values
    return question, correct_answer
