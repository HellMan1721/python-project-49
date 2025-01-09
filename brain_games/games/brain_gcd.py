import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gen_gamedata():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    random_numbers = f"{number_1} {number_2}"
    gcd_answer = f"{math.gcd(number_1, number_2)}"
    return random_numbers, gcd_answer
