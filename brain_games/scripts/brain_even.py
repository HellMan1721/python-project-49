import random

import brain_games.games.engine as game


def main():

    desc = 'Answer "yes" if the number is even, otherwise answer "no".'

    game.engine(desc, even)


def even():

    r = random.randint(1, 100)

    if r % 2 == 0:

        return r, 'yes'

    elif r != 0:

        return r, 'no'


if __name__ == '__main__':

    main()
