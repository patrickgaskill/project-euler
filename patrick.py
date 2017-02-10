from functools import reduce
from operator import mul
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
        
    if n == 2:
        return True

    if n == 3:
        return True

    if n % 2 == 0:
        return False

    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def prod(a):
    return reduce(mul, a)

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))
