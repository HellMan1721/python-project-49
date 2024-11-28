import brain_games.games.brain_even2 as be2
import brain_games.games.brain_calc as bc
import brain_games.games.brain_gcd as bg
import brain_games.games.brain_progression as gp
import brain_games.games.brain_prime as pr
import prompt
import random


def main():

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print('Hello, ' + name + '!')

    current_game = prompt.string('To select your Brain Game, plese enter the corresponding number:\n1. Even Numbers game.\n2. Brain Calculator game.\n3. GCD game.\n4. Progression game.\n5. Prime Numbers game.\n')

    all_games = ['1', '2', '3', '4', '5']

    if current_game == '1':

        print("Launching 'Even Numbers game'...")

    elif current_game == '2':

        print("Launching 'Brain Calculator game'...")

    elif current_game == '3':

        print("Launching 'GCD game'...")

    elif current_game == '4':

        print("Launching 'Progression game'...")

    elif current_game == '5':

        print("Launching 'Prime Numbers game'...")

    if current_game not in all_games:

        print('No game assigned for that number.\nGoodbye!')

        return None


    counter = 0


    while counter != 3:

        if current_game == '1':

            brain_question = be2.even2()

            correct_answer = be2.even1(brain_question)

        elif current_game == '2':

            calc_fund = bc.calc()

            brain_question = calc_fund[0]

            correct_answer = f"{calc_fund[1]}"

        elif current_game == '3':

            gcd_fund = bg.ran_gcd()

            brain_question = gcd_fund[0]

            correct_answer = f"{gcd_fund[1]}"

        elif current_game == '4':

            prog_fund = gp.gen_prog()

            brain_question = prog_fund[0]

            correct_answer = f"{prog_fund[1]}"

        elif current_game == '5':

            brain_question = random.randint(1, 100)

            correct_answer = pr.is_prime(brain_question)

        user_input = prompt.string(f"Question: {brain_question}\n")

        if user_input == correct_answer:

            print('Correct!')

            counter += 1

        elif user_input != correct_answer:

            print(f"'{user_input}' is wrong answer ;(. Correct answer was '{correct_answer}'.")

            print(f"Let's try again, {name}!")

            counter = 0


    print ('Congratulations!')


if __name__ == '__main__':

    main()
