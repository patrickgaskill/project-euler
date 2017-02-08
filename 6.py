NUMS = 100
sum_of_squares = sum(x ** 2 for x in range(NUMS + 1))
square_of_sum = sum(range(NUMS + 1)) ** 2
print(square_of_sum - sum_of_squares)
