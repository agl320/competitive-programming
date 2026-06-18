import math

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    if n > k:
        print(k)
    else:
        i = 1

        # # goal is the number to reach kth
        # while (n - 1) * (i + 1) < k:
        #     # each iteration, we are essentially checking n-1
        #     # for n = 3, k = 7
        #     # (4,5) (7,8) (10,11) (13,14)
        #     # for n = 4, k = 13
        #     # (5,6,7) (9,10,11) (13,14,15)

        #     i += 1

        # above loop can be simplified cuz geo. sum
        i = math.ceil((k / (n - 1)) - 1)

        # my brain melting
        # for j in range(1, n):
        #     print(n * i + j, end=",")

        rem = (k - n) % (n - 1)
        print(n * i + rem + 1)
