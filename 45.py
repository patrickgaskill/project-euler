def triangle(n):
    return (n * (n + 1)) // 2

def pentagonal(n):
    return (n * (3 * n - 1)) // 2

def hexagonal(n):
    return n * (2 * n - 1)

pentagonals = [1]
hexagonals = [1]

n = 286
while True:
    t = triangle(n)

    while pentagonals[-1] < t:
        pentagonals.append(pentagonal(len(pentagonals) + 1))

    while hexagonals[-1] < t:
        hexagonals.append(hexagonal(len(hexagonals) + 1))

    if t == pentagonals[-1] and t == hexagonals[-1]:
        print(t)
        break

    n += 1
