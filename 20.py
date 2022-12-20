import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

#Initial arrangement:
# 1, 2, -3, 3, -2, 0, 4

# 1 moves between 2 and -3:
# 2, 1, -3, 3, -2, 0, 4

# 2 moves between -3 and 3:
# 1, -3, 2, 3, -2, 0, 4

# -3 moves between -2 and 0:
# 1, 2, 3, -2, -3, 0, 4

# 3 moves between 0 and 4:
# 1, 2, -2, -3, 0, 3, 4

# -2 moves between 4 and 1:
# 1, 2, -3, 0, 3, 4, -2

# 0 does not move:
# 1, 2, -3, 0, 3, 4, -2

# 4 moves between -3 and 0:
# 1, 2, -3, 4, 0, 3, -2

# Write a function that moves the numbers as described above
# and returns the new list.


nums = []
for line in lines:
    nums.append(int(line))

for i in range(len(nums)):
    nums[i] = (nums[i], False)

def move(nums, i):
    print(nums)
    x = nums[i][0]
    if x < 0:
        newpos = (i + x - 1) % len(nums)
    else:
        newpos = (i + x ) % len(nums)
    nums.pop(i)
    nums.insert(newpos, (x, True)) 
    print(nums)
    print()

while True:
    moved = False
    for i in range(len(nums)):
        if not nums[i][1]:
            move(nums, i)
            moved = True
            break
    if not moved:
        break

print(nums)

