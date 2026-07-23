t = int(input())
for _ in range(t):
    a,b = list(map(int,input().split()))
    val = float('inf')
    for c in range(a,b):
        val = min((c-a) + (b-c),val)
    print(0 if val == float('inf') else val)