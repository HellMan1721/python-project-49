import prompt
import random
import brain_games.cli as cli


def main():

    name = cli.welcome_user()

    counter = 0

    while counter != 3:

        question = even2()

        user_answer = prompt.string(f"Question: {question}\n")

        correct_answer = even1(question)

        if user_answer == correct_answer:

            print('Correct!')

            counter += 1

        elif user_answer != correct_answer:

            print(f"'{user_answer}' is wrong answer ;(.")

            print(f"Correct answer was '{correct_answer}'.")

            print(f"Let's try again, {name}!")

            counter = 0

    print('Congratulations!')


def even1(i=0):

    if i % 2 == 0:

        return 'yes'

    elif i != 0:

        return 'no'


def even2():

    r = list(range(1, 100))

    random.shuffle(r)

    return r[random.randint(1, 100)]


if __name__ == '__main__':

    main()
