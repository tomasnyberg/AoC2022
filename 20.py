import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

nums = []
for idx, line in enumerate(lines):
    nums.append((int(line)*811589153, idx))
n = len(nums)
original = nums[:]

def move(nums, i):
    x, idx = nums[i]
    nums.pop(i)
    nums.insert((i + x) % (n-1), (x, idx))

for _ in range(10):
    for x, idx in original:
        i = nums.index((x, idx))
        move(nums, i)

zeroindex = 0
for i in range(n):
    if nums[i][0] == 0:
        zeroindex = i
        break
total = 0
for x in [1000, 2000, 3000]:
    total += nums[(zeroindex+x)%(n)][0]
print(total)
