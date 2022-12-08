import sys
lines = list(map(str.strip, sys.stdin.readlines()))

nums = []
for line in lines:
    curr = []
    for x in line:
        curr.append(int(x))
    nums.append(curr)

def dfs(istart, jstart):
    # up:
    result = 1
    up = 0
    for i in range(istart-1, -1, -1):
        if nums[i][jstart] >= nums[istart][jstart]:
            good = False
            up+=1
            break
        else:
            up += 1
    # down
    down = 0
    for i in range(istart+1, len(nums)):
        if nums[i][jstart] >= nums[istart][jstart]:
            good = False
            down += 1
            break
        else:
            down += 1
    right = 0
    for j in range(jstart-1, -1, -1):
        if nums[istart][j] >= nums[istart][jstart]:
            good = False
            right +=1
            break
        else:
            right += 1
    left = 0
    for j in range(jstart+1, len(nums[0])):
        if nums[istart][j] >= nums[istart][jstart]:
            good = False
            left += 1
            break
        else:
            left += 1
    print(up, down, left, right)
    return up * left*down * right
result = 0
dirs = [(-1, 0), (1,0), [0, 1], [0, -1]]
results = []
print(dfs(1, 2))
for i in range(len(nums)):
    for j in range(len(nums[0])):
        results.append(dfs(i, j))

print(max(results))

# all 4 directions in 2d
print(dirs)