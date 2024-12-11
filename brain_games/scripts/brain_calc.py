import random

import brain_games.games.engine as game


def main():

    desc = 'What is the result of the expression?'

    game.engine(desc, calc)


def calc():

    num_1 = random.randint(1, 100)

    num_2 = random.randint(1, 100)

    opers = ['+', '-', '*']

    ran_oper = random.choice(opers)

    a = f"{num_1} {ran_oper} {num_2}"

    b = f"{eval(a)}"

    return a, b


if __name__ == '__main__':

    main()
