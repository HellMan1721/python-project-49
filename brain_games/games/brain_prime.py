import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def gen_gamedata():
    random_number = random.randint(1, 100)
    question = f"{random_number}"
    if isPrime(random_number):
        return question, 'yes'
    else:
        return question, 'no'
