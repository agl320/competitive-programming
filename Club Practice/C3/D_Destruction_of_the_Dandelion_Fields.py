from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    # for _ in range(n):
    d = list(map(int,input().split()))

    d.sort()

    cut = 0
    odds = deque([])
    
    for dandelions in d:
        if dandelions%2 != 0:
            odds.append(dandelions)
        else:
            cut += dandelions
    
    if len(odds) <= 0:
        print(0)
    else:
        
        # [1, 3, 5, 6]
        off = True
        while len(odds) > 0:
            if off:
                c = odds.pop()
                cut += c
            else:
                odds.popleft()

            off = not off
        print(cut)

        # off, pop lowest odd
        # on, pop all even

        # on, pop highest odd -> off
        # off, pop lowest odd -> on

    

