import math
import random

DESC = 'Find the greatest common divisor of given numbers.'


def gen_gamedata():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    ran_num = f"{num_1} {num_2}"
    gcd_answer = f"{math.gcd(num_1, num_2)}"
    return ran_num, gcd_answer
