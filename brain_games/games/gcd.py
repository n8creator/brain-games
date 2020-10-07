"""Brain Game GCD Module."""

from random import randint
from math import gcd

GAME_INTRO = 'Find the greatest common divisor of given numbers.\n'
MIN_VALUE = 1
MAX_VALUE = 100


def generate_game():
    """Brain Games GCD Function.

    Function generates 2 random values and calculate GCD value using
    gcd() function from math module.

    Returns:
        tuple: question guessed to the user and correct answer
    """

    # Generate random numbers
    value_1, value_2 = randint(MIN_VALUE, MAX_VALUE), \
        randint(MIN_VALUE, MAX_VALUE)
    question = '{0} {1}'.format(value_1, value_2)

    # Calculate correct answer
    correct_answer = gcd(value_1, value_2)

    # Return function values
    return question, str(correct_answer)
