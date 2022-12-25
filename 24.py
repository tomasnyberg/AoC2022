import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

# all dirs in 4 directions
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
grid = list(map(list, lines))

blizzarddirs = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}

def simulate(grid, blizzards):
    new_blizzards = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in blizzards:
                for k in blizzards[(i, j)]:
                    di, dj = blizzarddirs[k]
                    ni, nj = i + di, j + dj
                    if grid[ni][nj] == '#':
                        ni, nj = (ni + 2*di) % len(grid), (nj + 2*dj) % len(grid[0])
                    if (ni, nj) not in new_blizzards: new_blizzards[(ni, nj)] = []
                    new_blizzards[(ni, nj)].append(k)
    return new_blizzards

def solve():
    pos = [0, 1]
    q = deque([pos])
    level = 0
    in_q = set([(0, 1)])
    count = 0
    p1ans = -1
    blizzards = {(i, j): grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] in ['<', '>', '^', 'v']}
    for i in range(1000):
        blizzards = simulate(grid, blizzards)
        level += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            in_q.remove((i, j))
            if count == 1 and i == 0 and j == 1:
                count += 1
                q = deque([(0, 1)])
                in_q = set([(0, 1)])
            if (count == 0 or count == 2) and i == len(grid) - 1 and j == len(grid[0]) - 2:
                if count == 0:
                    p1ans = level - 1
                elif count == 2:
                    return (p1ans, level - 1)
                count += 1
                q = deque([(len(grid) - 1, len(grid[0]) - 2)])
                in_q = set([q[0]])
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != '#' and (ni, nj) not in blizzards and (ni, nj) not in in_q:
                    q.append([ni, nj])
                    in_q.add((ni, nj))
    assert False
    
p1ans, p2ans = solve()
print("Part one:", p1ans)
print("Part two:", p2ans)
