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
for i in range(4):
    for xs in matrix:
        print(xs)
    print()
    for i in range(len(matrix)):
        sl = SortedList()
        for j in range(len(matrix)):
            if not sl or matrix[i][j] > sl[-1]:
                scored[i][j] = 1
            sl.add(matrix[i][j]) 
    rotateMatrix(matrix)
    rotateMatrix(scored)

for xs in scored:
    print(xs)

result = 0
for xs in scored:
    result += sum(xs)
print("Part one:", result)


# print("Part two:", p2res)