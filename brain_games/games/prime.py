"""Brain Game Prime Module."""

from random import randint

GAME_INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_RAND_VALUE = 1
MAX_RAND_VALUE = 20


def generate_round():
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

    # If number is lesser than 1, it is not prime
    if num < 2:
        return False
    # Check if the number has a multiple denominators
    for divider in range(2, round(num / 2) + 1):  # '+ 1' for case 'num == 4'
        if num % divider == 0:
            return False
    return True
