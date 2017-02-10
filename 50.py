from patrick import is_prime

LIMIT = 1000000

primes = [n for n in range(LIMIT // 2) if is_prime(n)]

for length in range(len(primes) - 1, 2, -1):

    done_with_this_length = False

    for start in range(0, len(primes) - length):

        s = sum(primes[start : start + length])

        if s >= LIMIT:
            done_with_this_length = True
            break

        if s < LIMIT and is_prime(s):
            print(s)
            quit()
