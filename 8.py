import sys
lines = list(map(str.strip, sys.stdin.readlines()))
matrix = [[int(y) for y in l] for l in lines]
n = len(matrix)

def part_one():
    def check(i1, j1):
        return all(matrix[i][j1] < matrix[i1][j1] for i in range(i1-1, -1, -1)) or \
               all(matrix[i][j1] < matrix[i1][j1] for i in range(i1+1, n)) or \
               all(matrix[i1][j] < matrix[i1][j1] for j in range(j1-1, -1, -1)) or \
               all(matrix[i1][j] < matrix[i1][j1] for j in range(j1+1, n))
    return sum(check(i, j) for i in range(n) for j in range(n))

def part_two():
    def dfs(i1, j1):
        result = 1
        for ud in [True, False]:
            dirsteps = [((i1 if ud else j1)-1, -1, -1), ((i1 if ud else j1)+1, n, 1)]
            for start, end, step in dirsteps:
                curr = 0
                for i in range(start, end, step):
                    curr += 1
                    if matrix[i if ud else i1][i if not ud else j1] >= matrix[i1][j1]:
                        break
                result *= curr
        return result
    return max(dfs(i, j) for i in range(n) for j in range(n))

print("Part one:", part_one())
print("Part two:", part_two())