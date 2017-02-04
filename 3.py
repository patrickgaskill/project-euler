from math import sqrt

def is_prime(n):
    return all(n % i for i in range(2, n))

def prime_factors(n):
    return list(filter(lambda x: n % x == 0 and is_prime(x), range(2, int(sqrt(n) / 2))))

print(prime_factors(600851475143)[-1])
