import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque
def show(grid):
    for row in grid:
        print(''.join(row))
    print()
# all dirs in 8 directions
dirs8 = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
# all dirs in 4 directions
dirs4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]

grid = [list(line) for line in lines]
# Add empty lines around the grid
for i in range(len(grid)):
    grid[i] = ['.']*200 + grid[i] + ['.']*200
for i in range(100):
    grid.insert(0, ['.']*len(grid[0]))
    grid.append(['.']*len(grid[0]))

triplets = deque([[(-1,0), (-1,-1), (-1, 1)], [(1, 0), (1,1), (1,-1)], [(0, -1), (-1, -1), (1, -1)], [(0, 1), (-1, 1), (1, 1)]])
show(grid)
def round():
    global grid
    proposed = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                # look in all 8 directions, count #s
                count = 0
                for di, dj in dirs8:
                    if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[i+di]):
                        if grid[i+di][j+dj] == '#':
                            count += 1
                if count == 0: continue
                # Check N, NE and NW
                for triplet in triplets:
                    count = 0
                    for di, dj in triplet:
                        if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[i]):
                            if grid[i+di][j+dj] == '#':
                                count += 1
                        else:
                            count += 1
                    if count == 0:
                        new = (i + triplet[0][0], j + triplet[0][1])
                        if new not in proposed: proposed[new] = []
                        # print("Elf at ", (i, j), "proposes to ", new)
                        proposed[new].append((i, j))
                        break
    # print(proposed)
    moved = 0
    for (i, j), xs in proposed.items():
        if len(xs) > 1: continue
        moved += 1
        grid[i][j] = '#'
        oi, oj = xs[0]
        grid[oi][oj] = '.'
    return moved == 0

for i in range(1000):
    if i == 10:
        lowestrow = 10**9
        lowestcol = 10**9
        highestrow =  -10**9
        highestcol = -10**9
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '#':
                    lowestrow = min(lowestrow, i)
                    highestrow = max(highestrow, i)
                    lowestcol = min(lowestcol, j)
                    highestcol = max(highestcol, j)
        result = 0
        for i in range(lowestrow, highestrow+1):
            for j in range(lowestcol, highestcol+1):
                if grid[i][j] == '.':
                    result += 1
        print("Part one:", result)
    if round():
        print("Part two:", i + 1)
        break
    x = triplets.popleft()
    triplets.append(x)

# find the highest row that has a #

