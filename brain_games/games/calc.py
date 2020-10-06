#!/usr/bin/env python3
"""Brain Calc game script."""

from random import randint, choice
import operator

GAME_INTRO = 'What is the result of the expression?\n'
MIN_RAND_VALUE, MAX_RAND_VALUE = 1, 10


def generate_game():
    """Brain-Game Calculator Script."""

    # Set list of allowed operators & select random operator for the game
    opearators_list = ['*', '-', '+']
    selected_operator = choice(opearators_list)

    # Set values used in the calc game
    value_1, value_2 = randint(MIN_RAND_VALUE, MAX_RAND_VALUE), \
        randint(MIN_RAND_VALUE, MAX_RAND_VALUE)

    # Ask user for a question
    question = str(value_1) + ' ' + selected_operator + ' ' + str(value_2)

    # Calculate correct answer (alternative to switch-case) by using dict{}
    correct_answer = {
        '*': operator.mul(value_1, value_2),
        '-': operator.sub(value_1, value_2),
        '+': operator.add(value_1, value_2)
    }[selected_operator]

    # Return function values
    return question, str(correct_answer)
