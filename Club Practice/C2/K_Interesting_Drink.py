n = int(input())

prices = list(map(int, input().split()))
days = int(input())

prices.sort()

for _ in range(days):
    coins = int(input())

    left = 0
    right = n
    while left < right:
        middle = left + (right - left) // 2

        if prices[middle] <= coins:
            left = middle + 1
        else:
            right = middle

    print(left)
