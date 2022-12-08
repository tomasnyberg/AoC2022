import sys
lines = list(map(str.strip, sys.stdin.readlines()))

matrix = [[int(y) for y in l] for l in lines]

def rotateMatrix(matrix):
    n = len(matrix)
    for x in range(0, int(n / 2)):
        for y in range(x, n-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = temp

def part_one():
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
    return sum(sum(xs) for xs in scored)

def part_two():
    def dfs(istart, jstart):
        result = 1
        for updown in [True, False]:
            for start, end, step in [((istart if updown else jstart)-1, -1, -1), ((istart if updown else jstart)+1, len(matrix), 1)]:
                curr = 0
                for i in range(start, end, step):
                    curr += 1
                    if matrix[i if updown else istart][i if not updown else jstart] >= matrix[istart][jstart]:
                        break
                result *= curr
        return result
    return max(dfs(i, j) for i in range(len(matrix)) for j in range(len(matrix)))


print("Part one:", part_one())
print("Part two:", part_two())