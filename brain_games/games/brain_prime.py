def is_prime(n):

    if n <= 1:

        return 'no'

    if n <= 3:

        return 'yes'

    if n % 2 == 0 or n % 3 == 0:

        return 'no'

    i = 5

    while i * i <= n:

        if n % i == 0 or n % (i + 2) == 0:

            return 'no'

        i += 6

    return 'yes'


if __name__ == '__main__':

    is_prime(5)
