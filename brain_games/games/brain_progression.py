import random

DESC = 'What number is missing in the progression?'


def gen():

    ran_length = random.randint(5, 15)

    ran_start = random.randint(1, 10)

    ran_step = random.randint(1, 10)

    ran_prog = list(range(ran_start, ran_start + ran_length * ran_step, ran_step))

    hid_index = random.randint(0, ran_length - 1)

    hid_value = f"{ran_prog[hid_index]}"

    ran_prog[hid_index] = '..'

    quest = ' '.join(str(i) for i in ran_prog)

    return quest, hid_value
