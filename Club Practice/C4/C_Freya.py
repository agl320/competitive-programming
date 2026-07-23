# travel x, then y, then x, etc.
# each jump is max k

import math

t = int(input())
for _ in range(t):
    x,y,k = list(map(int,input().split()))
    # number of x jumps
    # number of y jumps
    # number of jumps to ensure that x is equal or plus 1 of y

    x_jumps = math.ceil(x/k)
    y_jumps = math.ceil(y/k)
    if x_jumps < y_jumps:
        x_jumps = y_jumps

    if y_jumps < x_jumps:
        y_jumps = x_jumps - 1

    total = x_jumps+y_jumps
    print(total)