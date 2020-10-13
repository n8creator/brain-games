"""Brain Games Engine: the basic logic of the game described."""

import prompt

NUM_OF_ROUNDS = 3


def play_game(game_name):
    """Brain Game Engine function.

    Implemented a unified logic and workflow for all games in brain_games.games
    module (calc, even, gcd, progression and prime).

    Args:
        game_name (str): name of the game used in engine.
    """

    # Print Welcome message
    print('Welcome to Brain Games!')
    print(game_name.GAME_INTRO + '\n')

    # Ask user for his name and greet him
    name = prompt.string('May I have your name?: ')
    print('Hello, {0}!\n'.format(name))

    # Start game
    counter = 0
    while counter < NUM_OF_ROUNDS:
        # Getting question and correct_answer from game generator
        question, correct_answer = game_name.generate_round()

        # Ask user for question
        print('Question: ', question)
        user_answer = prompt.string('Your answer: ')

        # Check answer given by user
        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\
                " .format(user_answer, correct_answer))
            print("Let's try again, {0}!".format(name))

            # Exit from the game if at least one answer is incorrect
            exit()

    # Congratulate user if he correctrly answered for 3 questions
    print('Congratulations, {0}!'.format(name))
