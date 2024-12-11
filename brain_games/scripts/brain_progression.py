import random

import brain_games.games.engine as games


def main():

    desc = 'What number is missing in the progression?'

    games.engine(desc, gen_prog)


def gen_prog():

    ran_length = random.randint(5, 15)

    ran_start = random.randint(1, 10)

    ran_step = random.randint(1, 10)

    ran_prog = [ran_start + ran_step * i for i in range(ran_length)]

    hid_index = random.randint(0, ran_length - 1)

    hid_value = f"{ran_prog[hid_index]}"

    ran_prog[hid_index] = '..'

    quest = ' '.join(str(i) for i in ran_prog)

    return quest, hid_value


if __name__ == '__main__':

    main()
