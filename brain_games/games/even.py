#!/usr/bin/env python3
"""Brain Even game script."""

from random import randint
from brain_games.engine import greeting, get_username, ask_question, \
    check_answer, congratulate


def even():
    """@name Brani-Game Even Script."""

    greeting()
    print('Answer "yes" if number is Even otherwise answer "no".\n')
    name = get_username()

    for _ in range(1, 4):
        guess_value = randint(0, 100)

        user_answer = ask_question(guess_value)
        correct_answer = 'yes' if (guess_value % 2) == 0 else 'no'

        if check_answer(user_answer, correct_answer, name) is False:
            exit()

    congratulate(name)
