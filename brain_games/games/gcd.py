#!/usr/bin/env python3
"""Brain GCD game script."""

from random import randint
from math import gcd

GAME_INTRO = 'Find the greatest common divisor of given numbers.\n'
MIN_VALUE = 1
MAX_VALUE = 100


def generate_game():
    """@name Brain GCD data generator."""

    value_1, value_2 = randint(MIN_VALUE, MAX_VALUE), \
        randint(MIN_VALUE, MAX_VALUE)
    question = '{0} {1}'.format(value_1, value_2)
    correct_answer = gcd(value_1, value_2)

    return question, str(correct_answer)
