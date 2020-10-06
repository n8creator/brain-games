#!/usr/bin/env python3
"""Brain Prime game script."""

from random import randint
GAME_INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'
MIN_RAND_VALUE = 1
MAX_RAND_VALUE = 20


def generate_game():
    """@name Brain-Game data generator."""

    question = randint(MIN_RAND_VALUE, MAX_RAND_VALUE)
    correct_answer = 'yes' if is_Prime(question) else 'no'

    return question, correct_answer


def is_Prime(num):
    if num > 1:
        # Check if the number has a multiple denominators
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        # Number is prime if it doesn't have any denominators
        else:
            return True
    # If number is less than or equal to 1, it is not prime
    else:
        return False
