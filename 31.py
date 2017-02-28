def ways(amt, coins):
    if amt == 0:
        return 1
    elif not coins or amt < 0:
        return 0
    else:
        return ways(amt - coins[0], coins) + ways(amt, coins[1:])

print(ways(200, [200, 100, 50, 20, 10, 5, 2, 1]))
