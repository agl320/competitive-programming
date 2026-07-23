t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))  

    freq = {}
    for char in a:
        freq[char] = freq.get(char, 0) + 1

    valid = True
    max_freq = {}
    for char, char_freq in freq.items():
        if char_freq % k != 0:
            valid = False
            break
        else:
            max_freq[char] = char_freq // k   

    if not valid:
        print(0)
        continue



    window_count = {}
    l = 0
    awesome = 0

    for r in range(n):
        val = a[r]
        window_count[val] = window_count.get(val, 0) + 1

        while window_count[val] > max_freq[val]:
            left_val = a[l]
            window_count[left_val] -= 1
            l += 1

        awesome += r - l + 1

    print(awesome)