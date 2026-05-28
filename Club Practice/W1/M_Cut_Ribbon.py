n, a, b, c = list(map(int, input().split()))
dp = {}
key = sorted([a,b,c])

def explore(rem):
    if rem == 0:
        return 0
    elif rem < 0:
        return float('-inf')
    
    if rem in dp:
        return dp[rem]
    
    res = float('-inf')
    for k in key:
        res = max(explore(rem-k) + 1, res)

    dp[rem] = res
    return res

print(explore(n))

