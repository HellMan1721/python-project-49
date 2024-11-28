import random


def calc():

    num_1 = random.randint(1, 100)

    num_2 = random.randint(1, 100)

    opers = ['+', '-', '*']

    ran_oper = random.choice(opers)

    calc_quest = f"{num_1} {ran_oper} {num_2}"

    calc_answer = eval(calc_quest)

    return [calc_quest, calc_answer]


if __name__ == '__main__':

    calc()
