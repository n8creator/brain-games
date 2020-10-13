"""Brain Game Calculation Module."""

from random import randint, choice
import operator

GAME_INTRO = 'What is the result of the expression?\n'
MIN_RAND_VALUE, MAX_RAND_VALUE = 1, 10


def generate_game():
    """Brain Games Calculator Function.

    Function generates 2 random values and calculate result using random
    mathematical operator from the list.

    Returns:
        tuple: question guessed to the user and correct answer
    """

    # Set values used in the calc game
    value_1, value_2 = randint(MIN_RAND_VALUE, MAX_RAND_VALUE), \
        randint(MIN_RAND_VALUE, MAX_RAND_VALUE)

    # Set calculator available operations (alternative to switch-case)
    operations = {
        '*': operator.mul(value_1, value_2),
        '-': operator.sub(value_1, value_2),
        '+': operator.add(value_1, value_2),
    }

    # Select random operator from the list
    selected_operator = choice(list(operations.keys()))

    # Ask user for a question
    question = str(value_1) + ' ' + selected_operator + ' ' + str(value_2)

    # Calculate correct answer
    correct_answer = operations[selected_operator]

    # Return function values
    return question, str(correct_answer)
