from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    ans = deque([])
    for i in range(n):
        row = input()
        ans.appendleft(list(row).index("#")+1)
    for a in ans:
        print(a, end=" ")
    print()