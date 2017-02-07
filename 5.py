MAX_FACTOR = 20

i = MAX_FACTOR

while True:
    for j in range(2, MAX_FACTOR + 1):
        if (i % j != 0):
            i = i + MAX_FACTOR
            break
    else:
        break

print(i)
