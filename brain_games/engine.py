"""Brain Games engine: major functions described."""

import prompt


def greeting():
    """Print Welcome message."""
    print('Welcome to Brain Games!')


def get_username():
    """Ask user for his name and greet him"""
    name = prompt.string('May I have your name?: ')
    print('Hello, {0}!\n'.format(name))
    return name


def ask_question(question_expression):
    """Ask user for question."""
    print('Question: ', question_expression)
    return prompt.string('Your answer: ')


def check_answer(user_answer, correct_answer, name):
    """Check answer given by user."""
    if user_answer == correct_answer:
        print('Correct!')
    else:
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\
              " .format(user_answer, correct_answer))
        print("Let's try again, {0}!".format(name))
        return False


def congratulate(name):
    """Congratulate user if he correctrly answered for 3 questions"""
    print('Congratulations, {0}!'.format(name))
