t = int(input())

for _ in range(t):
    x,n = list(map(int,input().split()))

    if n%2 == 0:
        print(0)
    else:
        print(x)
