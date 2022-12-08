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

matrix = [[int(y) for y in l] for l in lines]
scored = [[0 for _ in l] for l in lines]
multiplication = [[1 for _ in l] for l in lines]
for iter in range(4):
    for i in range(len(matrix)):
        sl = SortedList()
        for j in range(len(matrix)):
            multiplication[i][j] *= sl.bisect_right(matrix[i][j])
            if not sl or matrix[i][j] > sl[-1]:
                scored[i][j] = 1
            sl.add(matrix[i][j]) 
    rotateMatrix(matrix)
    rotateMatrix(scored)
    rotateMatrix(multiplication)


result = 0
for xs in scored:
    result += sum(xs)
print("Part one:", result)
result = 0
for xs in multiplication:
    result = max(max(xs), result)
print("Part two:", result)