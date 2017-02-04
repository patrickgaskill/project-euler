fibs = [1, 2]
while True:
    if fibs[-1] + fibs[-2] > 4000000:
        break
    else:
        fibs.append(fibs[-1] + fibs[-2])

print(sum(filter(lambda x: x % 2 == 0, fibs)))
