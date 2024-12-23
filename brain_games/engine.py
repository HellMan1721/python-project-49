import prompt

import brain_games.cli as cli


def engine(game_module):

    name = cli.welcome_user()

    print(game_module.DESC)

    for i in range(0, 3):

        brain_question, correct_answer = game_module.game()

        user_input = prompt.string(f"Question: {brain_question}\n")

        if user_input == correct_answer:

            print('Correct!')

        elif user_input != correct_answer:

            print(f"'{user_input}' is wrong answer ;(.")

            print(f"Correct answer was '{correct_answer}'.")

            print(f"Let's try again, {name}!")

            break

    else:

        print(f"Congratulations, {name}!")
