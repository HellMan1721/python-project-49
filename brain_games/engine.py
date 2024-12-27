import prompt

ROUNDS = range(3)


def engine(game):

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print('Hello, ' + name + '!')

    print(game.DESC)

    for i in ROUNDS:

        brain_question, correct_answer = game.gen()

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
