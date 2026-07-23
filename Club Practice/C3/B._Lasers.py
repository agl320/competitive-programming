t = int(input())

for i in range(t):
    n,m,x,y = list(map(int,input().split()))

    c = 0

    # n is number of horizontal (y)
    lasers = list(map(int,input().split()))
    for l in lasers:
        if l >= 0 and l <= y:
            c += 1       

    # x
    lasers = list(map(int,input().split()))
    for l in lasers:
        if l >= 0 and l <= x:
            c += 1  
    
    print(c)