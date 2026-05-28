n, l = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

max_r = float('-inf')

max_r = max(max_r, nums[0])

for i in range(1, len(nums)):
    diff = nums[i] - nums[i-1]
    max_r = max(max_r, diff / 2)

max_r = max(max_r, l - nums[-1])

print(max_r)