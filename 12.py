import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))
start = [-1, -1]
end = [-1, -1]

starts = []
for i in range(len(lines)):
    lines[i] = list(lines[i])
    for j in range(len(lines[i])):
        if lines[i][j] == 'a':
            starts.append([i, j])
        if lines[i][j] == 'S':
            start = [i, j]
            lines[i][j] = 'a'
        if lines[i][j] == 'E':
            end = [i, j]
            lines[i][j] = 'z'

def bfs(start):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    q = [start]
    level = 0
    while tuple(end) not in visited:
        if not q:
            level = 10**9
            break
        for _ in range(len(q)):
            cur = q.pop(0)
            currchar = ord(lines[cur[0]][cur[1]])
            for d in dirs:
                new = [cur[0] + d[0], cur[1] + d[1]]
                # check inbounds
                if new[0] >= 0 and new[0] < len(lines) and new[1] >= 0 and new[1] < len(lines[0]):
                    otherchar = ord(lines[new[0]][new[1]])
                    if tuple(new) not in visited and (otherchar - currchar <= 1):
                        q.append(new)
                        visited.add(tuple(new))
        # grid the size of the matrix lines
        matrix = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]
        # for every visited nod, mark it as 1 in matrix
        for v in visited:
            matrix[v[0]][v[1]] = 1
        # print the matrix
        # for row in matrix:
        #     print(row)
        level += 1
    return level
print("Part one:", bfs(start))
result = 10**9
for start in starts:
    # print(count)
    result = min(result, bfs(start))
print("Part two:", result)







