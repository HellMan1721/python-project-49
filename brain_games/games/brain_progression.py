import random


def gen_prog():

    ran_length = random.randint(5, 15)

    ran_start = random.randint(1, 10)

    ran_step = random.randint(1, 10)

    ran_prog = [ran_start + ran_step * i for i in range(ran_length)]

    hid_index = random.randint(0, ran_length - 1)

    hid_value = ran_prog[hid_index]

    ran_prog[hid_index] = '..'

    return [ran_prog, hid_value]


if __name__ == '__main__':

    gen_prog()

