from patrick import is_prime

def truncations(s):
    return [s[:i] for i in range(1, len(s))] + [s[i:] for i in range(1, len(s))]

def has_prime_truncations(n):
    return all(is_prime(int(s)) for s in truncations(str(n)))

i = 11
truncatable_primes = []

while True:
    if (is_prime(i) and has_prime_truncations(i)):
        truncatable_primes.append(i)

    if len(truncatable_primes) >= 11:
        break

    i += 1

print(sum(truncatable_primes))
