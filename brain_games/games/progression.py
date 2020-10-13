#!/usr/bin/env python3
"""Brain Progression game script."""

from random import randint, choice

GAME_INTRO = 'What number is missing in the progression?'
MIN_PROGR_VALUE, MAX_PROGR_VALUE = 1, 100
MIN_STEP_VALUE, MAX_STEP_VALUE = 1, 10
PROGRESSION_LENGTH = 10


def generate_round():
    """Brain Games Progression Function.

    Generates arithmetic progression list using some random values. Then
    hiding some random value in progression list.

    Returns:
        tuple: question guessed to the user and correct answer
    """

    # Set arythmetic progression values
    value, step = randint(MIN_PROGR_VALUE, MAX_PROGR_VALUE), \
        randint(MIN_STEP_VALUE, MAX_STEP_VALUE)

    # Generate progression list with values in it
    progress_list = []
    for _ in range(0, PROGRESSION_LENGTH):
        progress_list.append(str(value))
        value += step

    # Select random value in progression list
    correct_answer = choice(progress_list)
    answer_index = progress_list.index(correct_answer)

    # Hide selected value in progression list
    progress_list[answer_index] = '..'

    # Ask user for a question
    question = ' '.join(progress_list)

    # Return function values
    return question, correct_answer
