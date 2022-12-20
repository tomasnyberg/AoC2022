import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

nums= [(int(line), idx) for idx, line in enumerate(lines)]
n, original = len(nums), nums[:]

def move(nums, i):
    x, idx = nums[i]
    nums.pop(i)
    nums.insert((i + x) % (n-1), (x, idx))

def mix():
    for x, idx in original:
        i = nums.index((x, idx))
        move(nums, i)

def part_one():
    mix()
    zeroindex = [x for x, _ in nums].index(0)
    print("Part one:", sum([nums[(zeroindex+x)%(n)][0] for x in [1000, 2000, 3000]]))

def part_two():
    global original
    global nums
    nums = original[:]
    for i in range(len(nums)):
        nums[i] = (nums[i][0] * 811589153, nums[i][1])
    original = nums[:]
    for _ in range(10):
        mix()
    zeroindex = [x for x, _ in nums].index(0)
    print("Part two:", sum([nums[(zeroindex+x)%(n)][0] for x in [1000, 2000, 3000]]))

part_one()
part_two()