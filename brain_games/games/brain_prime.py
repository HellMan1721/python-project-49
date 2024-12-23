import random


def game():

    n = random.randint(1, 100)

    question = f"{n}"

    if n <= 1:

        return question, 'no'

    if n <= 3:

        return question, 'yes'

    if n % 2 == 0 or n % 3 == 0:

        return question, 'no'

    i = 5

    while i * i <= n:

        if n % i == 0 or n % (i + 2) == 0:

            return question, 'no'

        i += 6

    return question, 'yes'


DESC = 'Answer "yes" if given number is prime. Otherwise answer "no".'
