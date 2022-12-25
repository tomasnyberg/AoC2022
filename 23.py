import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

dirs4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dirs8 = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

grid = [list(line) for line in lines]
for i in range(len(grid)):
    grid[i] = ['.']*200 + grid[i] + ['.']*200
for i in range(100):
    grid.insert(0, ['.']*len(grid[0]))
    grid.append(['.']*len(grid[0]))

triplets = deque([[(-1,0), (-1,-1), (-1, 1)], [(1, 0), (1,1), (1,-1)], [(0, -1), (-1, -1), (1, -1)], [(0, 1), (-1, 1), (1, 1)]])

def round():
    def empty_around_check(i, j, directions):
        for di, dj in directions:
            if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[i+di]):
                if grid[i+di][j+dj] == '#':
                    return False
        return True
    proposed = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                if empty_around_check(i, j, dirs8): continue
                for triplet in triplets:
                    if empty_around_check(i, j, triplet):
                        new = (i + triplet[0][0], j + triplet[0][1])
                        if new not in proposed: proposed[new] = []
                        proposed[new].append((i, j))
                        break
    moved = 0
    for (i, j), xs in proposed.items():
        if len(xs) > 1: continue
        moved += 1
        grid[i][j] = '#'
        grid[xs[0][0]][xs[0][1]] = '.'
    return moved == 0

for i in range(1000):
    if i == 10:
        minmaxes = [10**9, 10**9, -10**9, -10**9]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '#':
                    minmaxes[0] = min(minmaxes[0], i)
                    minmaxes[1] = min(minmaxes[1], j)
                    minmaxes[2] = max(minmaxes[2], i)
                    minmaxes[3] = max(minmaxes[3], j)
        result = 0
        for i in range(minmaxes[0], minmaxes[2]+1):
            for j in range(minmaxes[1], minmaxes[3]+1):
                if grid[i][j] == '.':
                    result += 1
        print("Part one:", result)
    if round():
        print("Part two:", i + 1)
        break
    x = triplets.popleft()
    triplets.append(x)
