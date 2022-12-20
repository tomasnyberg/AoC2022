import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

nums= [(int(line)*811589153, idx) for idx, line in enumerate(lines)]
n, original = len(nums), nums[:]

def move(nums, i):
    x, idx = nums[i]
    nums.pop(i)
    nums.insert((i + x) % (n-1), (x, idx))

for round in range(10):
    for x, idx in original:
        i = nums.index((x, idx))
        move(nums, i)

zeroindex = [x for x, _ in nums].index(0)
print("Part two:", sum([nums[(zeroindex+x)%(n)][0] for x in [1000, 2000, 3000]]))
