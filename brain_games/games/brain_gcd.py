import math
import random


def game():

    num_1 = random.randint(1, 100)

    num_2 = random.randint(1, 100)

    ran_num = f"{num_1} {num_2}"

    gcd_answer = f"{math.gcd(num_1, num_2)}"

    return ran_num, gcd_answer


DESC = 'Find the greatest common divisor of given numbers.'
