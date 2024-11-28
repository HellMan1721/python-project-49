import random


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

    even1()
    even2()
