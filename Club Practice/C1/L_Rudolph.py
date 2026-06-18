import math
t = int(input())

for i in range(t):
    n, d, h = map(int, input().split())
    y = sorted(list(map(int,input().split())))

    total_area = n * d * h / 2

    overlap = 0

    for i in range(n-1):
        gap = y[i+1] - y[i]
        if gap < h:
            y_overlap = h - gap
            overlap += d * y_overlap * y_overlap /(2*h)

    print(total_area - overlap)
