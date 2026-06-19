t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    # x < z < y
    # y is not divisible by z (y is not a multiple of z, y is not made of z)
    # z is divisible by x (z is multiple of x, z is made of x)
    # y is divisible by x

    # find a number that is divisible by x but y is not divisible by it
    # cx = z
    # y % m(cx) != 0 
    # y % cx = 0
    # y % m != 0
    #  
    # y % z != 0
    # m(ax) % (bx)

    ans = "NO"
    for m in range(x+1,y):
        
        if y%m != 0:
            ans = "YES"
            break
    print(ans)