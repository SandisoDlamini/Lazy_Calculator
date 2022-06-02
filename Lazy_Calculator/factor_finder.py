from functools import reduce
from math import sqrt


def take_input(n):
    n = str(n)
    if len(n) <= 4:
        find_factors(int(n))
    else:
        factors_fast(int(n))


def factors_fast(n):
    step = 2 if n % 2 else 1
    fs = set(reduce(list.__add__,
                    ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))

    df = tuple(sorted(list(fs)))
    if not df:
        print('The factor of ' + str(n) + ' is 1.')
    else:
        print('The factors of ' + str(n) + ' are ' + str(df) + '.')


def find_factors(n):
    """Find the factors of numbers."""
    f = []
    for i in range(1, n):
        if n % i == 0:
            a = n / i
            if a not in f:
                f.extend((int(a), int(i)))
                f.sort()
    factors = tuple(f)

    if n == 0:
        print('Zero has no factors.')
    elif not factors:
        print(f'The factor of {str(n)} is 1.')
    else:
        print(f'The factors of {str(n)} are {factors}.')
