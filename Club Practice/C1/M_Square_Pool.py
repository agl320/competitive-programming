
t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    count = 0
    for i in range(n):
        dx, dy, x, y = map(int, input().split())
        if dx * dy == 1:  
            if x == y:
                count += 1
        else:  
            if x + y == s:
                count += 1

    print(count)
