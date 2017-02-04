from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

def prime_factors(n):
    return list(filter(lambda x: n % x == 0 and is_prime(x), islice(count(2), int(sqrt(n)-1))))

print(prime_factors(600851475143)[-1])
