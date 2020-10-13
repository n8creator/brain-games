"""Brain Game Prime Module."""

from random import randint

GAME_INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'
MIN_RAND_VALUE = 1
MAX_RAND_VALUE = 20


def generate_game():
    """Brain Games Prime Function.

    Function generates some random value and checks if this numuber is prime
    using is_Prime() function.

    Returns:
        tuple: question guessed to the user and correct answer
    """

    # Generate random numbers
    question = randint(MIN_RAND_VALUE, MAX_RAND_VALUE)

    # Calculate correct answer
    correct_answer = 'yes' if is_prime(question) else 'no'

    # Return function values
    return question, correct_answer


def is_prime(num):
    """Checks if num value is prime.

    A prime number is a natural number greater than 1 that is not a
    product of two smaller natural numbers.

    Args:
        num (int): checked number

    Returns:
        bool: True if value is prime, False otherwise.
    """

    if num > 1:
        # Check if the number has a multiple denominators
        for i in range(2, num):
            # Number is prime if it doesn't have any denominators
            return False if (num % i) == 0 else True

    # If number is less than or equal to 1, it is not prime
    else:
        return False
