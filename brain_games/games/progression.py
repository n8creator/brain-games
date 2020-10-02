#!/usr/bin/env python3
"""Brain Progression game script."""

from random import randint, choice
from brain_games.engine import greeting, get_username, ask_question, \
    check_answer, congratulate


def brain_progression():
    """@name Brain-Game Progression Script."""

    greeting()
    print("What number is missing in the progression?\n")
    name = get_username()

    for _ in range(1, 4):
        # Generate progression list
        value, step = randint(1, 100), randint(1, 10)
        progress_list = []

        for _ in range(0, 10):
            progress_list.append(str(value))
            value += step

        # Selecting random value in progression list and Hiding it
        correct_answer = choice(progress_list)
        answer_index = progress_list.index(correct_answer)
        progress_list[answer_index] = '..'

        # Asking user for a question
        expression = ' '.join(progress_list)
        user_answer = ask_question(expression)

        # Check user answer
        if check_answer(user_answer, correct_answer, name) is False:
            exit()

    congratulate(name)
