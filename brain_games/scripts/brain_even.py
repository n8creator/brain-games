#!/usr/bin/env python3
"""Hexlet 1-st project, brain_even game."""

from random import randint

import prompt


def brain_even(name):
    """@name Brain even main script."""
    attempts, correct_counter = 3, 0
    while attempts > 0:
        guess_value = randint(0, 100)

        print('If this number even or not?: ', guess_value)
        user_answer = prompt.string('Your answer (yes/no): ')

        correct_answer = 'yes' if (guess_value % 2) == 0 else 'no'
        if user_answer == correct_answer:
            print('Correct!')
            correct_counter += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'."
                  .format(user_answer, correct_answer))
            print("Let's try again, {0}!".format(name))
            break
        attempts -= 1

    if correct_counter == 3:
        print('Congratulations, {0}!'.format(name))


def main():
    """Welcome user and greet him."""
    print('Welcome to Brain Games!')
    print('Answer "yes" if number even otherwise user_answer "no".\n')
    name = prompt.string('May I have your name?: ')
    print('Hello, {0}!\n'.format(name))

    # brain_even() code insert
    brain_even(name)


if __name__ == '__main__':
    main()
