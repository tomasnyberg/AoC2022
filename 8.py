import sys
lines = list(map(str.strip, sys.stdin.readlines()))

matrix = [[int(y) for y in l] for l in lines]
nums = matrix
n, m = len(matrix), len(matrix[0])

def score(istart, jstart):
    dirs = [(-1, 0), (1,0), [0, 1], [0, -1]]
    def dfs(i, j, di, dj):
        if i < 0 or j < 0 or i == len(matrix) or j == len(matrix[0]) or matrix[i][j] >= matrix[istart][jstart]:
            return 0
        return 1 + dfs(i + di, j +dj, di, dj)
    results = []
    for di, dj in dirs:
        results.append(dfs(istart+di, jstart+dj, di, dj))
    return results

def visible(i, j):
    scores = score(i, j)
    return scores[0] == i or scores[1] == n - i - 1 or scores[2] == m-j-1 or scores[3] == j
print(score(0, 0))
print(visible(0, 0))

def scenic(i, j):
    result = 1
    for x in score(i, j):
        result *= x
    return result

p1res = 0
p2res = 0
for i in range(len(nums)):
    for j in range(len(nums[0])):
        if visible(i, j):
            print(i, j, "is visible")
            p1res += 1
        p2res = max(p2res, scenic(i, j))

print("Part one:", p1res)
print("Part two:", p2res)