from itertools import islice, count
from patrick import is_prime, factors

def prime_factors(n):
    return list(filter(is_prime, factors(n)))

print(prime_factors(600851475143)[-1])
