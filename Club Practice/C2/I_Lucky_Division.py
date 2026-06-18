n = int(input())

lucky_numbers = [4, 7, 47, 74, 444, 447, 477, 777, 774, 744]

lucky = "NO"
for l in lucky_numbers:
    if n % l == 0:
        lucky = "YES"
        break

print(lucky)
