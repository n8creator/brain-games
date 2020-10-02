#!/usr/bin/env python3
"""Brain GCD game script."""

from random import randint
from math import gcd
from brain_games.engine import greeting, get_username, ask_question, \
    check_answer, congratulate


def brain_gcd():
    """@name Brain-Game GCD Script."""

    greeting()
    print('Find the greatest common divisor of given numbers.\n')
    name = get_username()

    for _ in range(1, 4):
        value_1, value_2 = randint(1, 100), randint(1, 100)

        user_answer = int(ask_question('{0} {1}'.format(value_1, value_2)))
        correct_answer = gcd(value_1, value_2)

        if check_answer(user_answer, correct_answer, name) is False:
            exit()

    congratulate(name)
