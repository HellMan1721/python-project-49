import prompt
import brain_games.scripts.brain_games as bg


def engine(fn):

    name = bg.main()

    counter = 0

    while counter != 3:

        brain_question, correct_answer = fn()

        user_input = prompt.string(f"Question: {brain_question}\n")

        if user_input == correct_answer:

            print('Correct!')

            counter += 1

        elif user_input != correct_answer:

            print(f"'{user_input}' is wrong answer ;(.")

            print(f"Correct answer was '{correct_answer}'.")

            print(f"Let's try again, {name}!")

            counter = 0

    print('Congratulations!')
