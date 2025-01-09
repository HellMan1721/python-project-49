import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gen_gamedata():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    random_numbers = f"{num_1} {num_2}"
    gcd_answer = f"{math.gcd(num_1, num_2)}"
    return random_numbers, gcd_answer
