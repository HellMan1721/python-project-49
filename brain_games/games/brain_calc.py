import random

DESC = 'What is the result of the expression?'


def gen():

    num_1 = random.randint(1, 100)

    num_2 = random.randint(1, 100)

    opers = ['+', '-', '*']

    ran_oper = random.choice(opers)

    question = f"{num_1} {ran_oper} {num_2}"

    if ran_oper == '+':

        result = num_1 + num_2

    elif ran_oper == '-':

        result = num_1 - num_2

    elif ran_oper == '*':

        result = num_1 * num_2

    answer = f'{result}'

    return question, answer
