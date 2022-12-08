import sys
lines = list(map(str.strip, sys.stdin.readlines()))

matrix = [[int(y) for y in l] for l in lines]

def part_one():
    def check(i1, j1):
        return all(matrix[i][j1] < matrix[i1][j1] for i in range(i1-1, -1, -1)) or \
               all(matrix[i][j1] < matrix[i1][j1] for i in range(i1+1, len(matrix))) or \
               all(matrix[i1][j] < matrix[i1][j1] for j in range(j1-1, -1, -1)) or \
               all(matrix[i1][j] < matrix[i1][j1] for j in range(j1+1, len(matrix)))
    return sum(check(i, j) for i in range(len(matrix)) for j in range(len(matrix)))

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