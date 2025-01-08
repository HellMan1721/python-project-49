import random

DESC = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def gen_gamedata():
    n = random.randint(1, 100)
    question = f"{n}"
    if isPrime(n):
        return question, 'yes'
    else:
        return question, 'no'
