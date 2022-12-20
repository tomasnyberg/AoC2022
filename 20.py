import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

nums = []
for idx, line in enumerate(lines):
    nums.append((int(line), idx, False))
n = len(nums)

def move(nums, i):
    x = nums[i][0]
    nums[i] = (x, i, True)
    nums.pop(i)
    new = (i + x) % (n-1)
    nums.insert(new, (x, i, True))

while True:
    moved = False
    for i in range(len(nums)):
        if not nums[i][2]:
            move(nums, i)
            moved = True
            break
    if not moved:
        break

zeroindex = 0
for i in range(n):
    if nums[i][0] == 0:
        zeroindex = i
        break
total = 0
for x in [1000, 2000, 3000]:
    total += nums[(zeroindex+x)%(n)][0]
print(total)
