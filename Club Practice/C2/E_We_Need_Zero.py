# 1 2 2 3
# 0001 0010 0010 0011
# 0010

# X = 1 xor 2 xor 2 xor 3


t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    x = 0
    for i in a:
        x ^= i

    if n % 2 == 0:
        if x == 0:
            print(1)
        else:
            print(-1)
    else:
        print(x)
