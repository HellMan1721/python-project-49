import random

DESC = 'Answer "yes" if the number is even, otherwise answer "no".'


def gen_gamedata():
    r = random.randint(1, 100)
    if r % 2 == 0:
        return r, 'yes'
    elif r != 0:
        return r, 'no'
