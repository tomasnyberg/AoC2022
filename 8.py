import sys
from sortedcontainers import SortedList
lines = list(map(str.strip, sys.stdin.readlines()))

def rotateMatrix(matrix):
    n = len(matrix)
    for x in range(0, int(n / 2)):
        for y in range(x, n-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = temp

def dfs(istart, jstart):
    # up:
    result = 1
    for start, end, step in [(istart-1, -1, -1), (istart+1, len(matrix), 1)]:
        curr = 0
        for i in range(start, end, step):
            if matrix[i][jstart] >= matrix[istart][jstart]:
                curr += 1
                break
            else:
                curr += 1
        result *= curr
    for start, end, step in [(jstart-1, -1, -1), (jstart+1, len(matrix[0]), 1)]:
        curr = 0
        for j in range(start, end, step):
            if matrix[istart][j] >= matrix[istart][jstart]:
                curr += 1
                break
            else:
                curr += 1
        result *= curr
    return result
    
matrix = [[int(y) for y in l] for l in lines]
scored = [[0 for _ in l] for l in lines]
for iter in range(4):
    for i in range(len(matrix)):
        biggest = -1
        for j in range(len(matrix)):
            if matrix[i][j] > biggest:
                scored[i][j] = 1
                biggest = matrix[i][j]
    for m in [matrix, scored]:
        rotateMatrix(m)

best = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        best = max(best, dfs(i, j))

result = 0
for xs in scored:
    result += sum(xs)
print("Part one:", result)
result = 0
print("Part two:", best)