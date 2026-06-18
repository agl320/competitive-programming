n = int(input())
cards = list(map(int, input().split()))

l = 0
r = n - 1

a = b = 0
turn = False

while l <= r:
    if cards[l] >= cards[r]:
        val = cards[l]
        l += 1
    else:
        val = cards[r]
        r -= 1

    if turn:
        a += val
    else:
        b += val

    turn = not turn

print(b, a)
