import sys, re
grid = list(map(lambda x: list(x.strip()), sys.stdin.readlines()))
n, m = len(grid), len(grid[0])

start = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 'S'][0]
end = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 'E'][0]
grid[start[0]][start[1]] = 'a'
grid[end[0]][end[1]] = 'z'

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(start, end, p2=False):
    def good_check(p2, curr, other):
        return (p2 and (other - curr >= -1)) or (not p2 and other - curr <= 1)
    visited = set()
    q = [start]
    level = 0
    while end not in visited:
        for _ in range(len(q)):
            cur = q.pop(0)
            currchar = ord(grid[cur[0]][cur[1]])
            if p2 and currchar == 97: return level
            for d in dirs:
                new = (cur[0] + d[0], cur[1] + d[1])
                if 0 <= new[0] < len(grid) and 0 <= new[1] < len(grid[0]):
                    otherchar = ord(grid[new[0]][new[1]])
                    if new not in visited:
                        if good_check(p2, currchar, otherchar):
                            q.append(new)
                            visited.add(new)
        level += 1
    return level

print("Part one:", bfs(start, end))
print("Part two:", bfs(end, start, True))
