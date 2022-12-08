import sys
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
            curr += 1
            if matrix[i][jstart] >= matrix[istart][jstart]:
                break
        result *= curr
    for start, end, step in [(jstart-1, -1, -1), (jstart+1, len(matrix[0]), 1)]:
        curr = 0
        for j in range(start, end, step):
            curr += 1
            if matrix[istart][j] >= matrix[istart][jstart]:
                break
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

print("Part one:", sum(sum(xs) for xs in scored))
print("Part two:", max(dfs(i, j) for i in range(len(matrix)) for j in range(len(matrix))))