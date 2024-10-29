import random
import prompt


def main():

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print('Hello, ' + name + '!')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0

    while counter != 3:

        number = random.randint(1, 100)

        test = prompt.string(f"Question: {number}\n")

        if number % 2 == 0:

            if test == 'yes':

                print('Correct!')

                counter += 1

            elif test != 'yes':

                print(f"'{test}' is wrong answer ;(. Correct answer was 'yes'.")

                print(f"Let's try again, {name}!")

                counter = 0

        elif number % 2 != 0:

            if test == 'no':

                print('Correct!')

                counter += 1

            elif test != 'no':

                print(f"'{test}' is wrong answer ;(. Correct answer was 'no'.")

                print(f"Let's try again, {name}!")

                counter = 0

    print(f"Congratulations, {name}!")


if __name__ == '__main__':

    main()
