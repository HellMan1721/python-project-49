import random
import math
import brain_games.games.engine as game


def main():

    game.engine(brain_gcd)


def brain_gcd():

    num_1 = random.randint(1, 100)

    num_2 = random.randint(1, 100)

    ran_num = f"{num_1} {num_2}"

    gcd_answer = f"{math.gcd(num_1, num_2)}"

    return ran_num, gcd_answer


if __name__ == '__main__':

    main()
