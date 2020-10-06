"""Brain Even data generator."""

from random import randint
GAME_INTRO = 'Answer "yes" if number is Even otherwise answer "no".\n'
MIN_VALUE, MAX_VALUE = 1, 100


def generate_game():
    """@name Brain Even data generator."""

    # Generate ranom number
    question = randint(MIN_VALUE, MAX_VALUE)

    # Check if generated number is even
    correct_answer = 'yes' if (question % 2) == 0 else 'no'

    # Return function values
    return question, correct_answer
