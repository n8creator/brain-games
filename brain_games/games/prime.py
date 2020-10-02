#!/usr/bin/env python3
"""Brain Prime game script."""

from random import randint
from brain_games.engine import greeting, get_username, ask_question, \
    check_answer, congratulate
from brain_games.functions import is_Prime


def brain_prime():
    """@name Brain-Game Prime Script."""

    greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".\n')
    name = get_username()

    for _ in range(1, 4):
        value = randint(1, 20)

        user_answer = ask_question(value)
        correct_answer = 'yes' if is_Prime(value) else 'no'

        if check_answer(user_answer, correct_answer, name) is False:
            exit()

    congratulate(name)
