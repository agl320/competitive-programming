t = int(input())
for i in range(t):
    n = int(input())
    message = input()

    res = []

    i = 0

    while i < n:
        c = message[i]
        res.append(c)

        j = i + 1
        while message[j] != c:
            j += 1

        i = j + 1

    print("".join(x for x in res))
