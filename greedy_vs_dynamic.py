coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    change = dict()
    if amount == 0:
        return 0

    for i in coins:
        if i <= amount:
            count = amount // i 
            change[i] = count 
            amount -= count * i  

    return change


def find_min_coins(amount):
    change = dict()
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    i = amount
    for coin in coins:
        while i - coin >= 0 and dp[i] == dp[i - coin] + 1:
            if coin not in change:
                change[coin] = 0
            change[coin] += 1
            i -= coin

    return change
