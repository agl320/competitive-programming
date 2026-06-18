# x and y
# y is multiple of x (y is divisible by x)

# find z, y > z > x
# z is multiple of x (z is divisible by x)
# y is not multiple of z

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    verdict = "NO"
    for z in range(x + 1, y - 1):
        if z % y != 0 and z % x == 0:
            verdict = "YES"
            break
    print(verdict)
