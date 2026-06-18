

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))

t = int_input()
for i in range(t):
    n = int_input()
    vals = list_input()

    num = 0

    for j in range(8):
        count_1 = 0
        for v in vals:
            if (v >> j) & 1:
                count_1 += 1
        
        if count_1 % 2 != 0:
            num = num | (1 << j)
    
    print(num)
