#!/usr/bin/env python3
"""Brain Calc game script."""

from random import randint, choice
from brain_games.engine import greeting, get_username, ask_question, \
    check_answer, congratulate


def calc():
    """Brain-Game Calculator Script."""

    greeting()
    print('What is the result of the expression?\n')
    name = get_username()

    opearators_list = ['*', '-', '+']

    for _ in range(1, 4):
        val_1, val_2 = randint(0, 10), randint(0, 10)
        operator = choice(opearators_list)
        expression = str(val_1) + ' ' + operator + ' ' + str(val_2)

        user_answer = int(ask_question(expression))
        correct_answer = int(eval(expression))

        if check_answer(user_answer, correct_answer, name) is False:
            exit()

    congratulate(name)
