

t = int(input())

for _ in range(t):
    requirements,minutes = list(map(int,input().split()))

    stays = 0
    crossed = False
    for _ in range(requirements):
        a,b = list(map(int,input().split()))

        # 2,1 
        # 2nd minute, must be at side 1
        # 1st minute -> 1
        # 2nd minute -> stay

        # does not have to stay
        
        if not crossed:
            if (a%2 != 0 and b == 0 or a%2 == 0 and b == 1):
                stays += 1
                crossed = not crossed
        else:
            if (a%2 != 0 and b == 1 or a%2 == 0 and b == 0):
                stays += 1
                crossed = not crossed
            
    print(minutes - stays)




