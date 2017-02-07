NUMS = 100
sum_of_squares = sum(map(lambda x: x ** 2, range(NUMS + 1)))
square_of_sum = sum(range(NUMS + 1)) ** 2
print(square_of_sum - sum_of_squares)
