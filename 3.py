from itertools import islice, count
from patrick import is_prime

def prime_factors(n):
    return list(filter(lambda x: n % x == 0 and is_prime(x), islice(count(2), int(n ** 0.5 - 1))))

print(prime_factors(600851475143)[-1])
