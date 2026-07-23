t = int(input())

for _ in range(t):
    n = int(input())

    # x vals
    upper = set()
    lower = set()

    for _ in range(n):
        x, y = map(int, input().split())

        if y == 1:
            upper.add(x)
        else:
            lower.add(x)

    #print(upper,lower)
    ans = 0


    # right triangle can only be formed by +1,-1 since y+-1
    for x in upper:
        if x - 1 in lower and x + 1 in lower:
            ans += 1

    for x in lower:
        if x - 1 in upper and x + 1 in upper:
            ans += 1

    # all are solutions
    common = upper & lower

    for x in common:
        ans += len(lower) - 1
        ans += len(upper) - 1

    print(ans)