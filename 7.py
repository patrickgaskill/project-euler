from patrick import is_prime

N = 10001

primes = [2, 3]
i = primes[-1] + 2

while len(primes) < N:
    if (is_prime(i)):
        primes.append(i)
    i += 2

print(primes[-1])
