from functools import reduce
from patrick import is_prime, factors

ORDER = 4

def consec(n, k):
    return [n + i for i in range(k)]

def prime_factors(n):
    return [f for f in factors(n) if is_prime(f)]

n = 2
while True:
    if all(len(prime_factors(n)) >= ORDER for n in consec(n, ORDER)):
        print(n)
        break
    n += 1
