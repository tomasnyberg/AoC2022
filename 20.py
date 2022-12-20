import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))
KEY = 811589153

nums = []
for idx, line in enumerate(lines):
    nums.append((int(line)*KEY, idx))
n = len(nums)

original = nums[:]

def move(nums, i):
    x, idx = nums[i]
    # nums[i] = (x, i)
    nums.pop(i)
    new = (i + x) % (n-1)
    nums.insert(new, (x, idx))

for _ in range(10):
    print([nums[i] for i in range(len(nums))])
    for x, idx in original:
        # print("moving", idx)
        i = nums.index((x, idx))
        move(nums, i)
    print([nums[i] for i in range(len(nums))])
    print()

zeroindex = 0
for i in range(n):
    if nums[i][0] == 0:
        zeroindex = i
        break
total = 0
for x in [1000, 2000, 3000]:
    total += nums[(zeroindex+x)%(n)][0]
print(total)
