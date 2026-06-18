t = int(input())

for i in range(t):
    n = int(input())

    str_n = str(n)
    min_digit = 9
    for digit in str_n:
        min_digit = min(min_digit, int(digit))

    print(min_digit)
