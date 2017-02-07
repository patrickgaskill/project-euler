from patrick import is_prime

MAX = 2000000

print(2 + sum(filter(is_prime, range(3, MAX, 2))))
