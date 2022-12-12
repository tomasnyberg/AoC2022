import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))
nums = []
start = [-1, -1]
end = [-1, -1]
for line in lines:
    line = list(line)

starts = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'a':
            starts.append([i, j])
        if lines[i][j] == 'S':
            start = [i, j]
        if lines[i][j] == 'E':
            end = [i, j]

# lines[start[0]][start[1]] = 'a'
# lines[end[0]][end[1]] = 'z'


def bfs(start, count):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    q = [start]
    level = 0
    while tuple(end) not in visited:
        # do a bfs
        if not q:
            level = 10**9
            break
        for i in range(len(q)):
            cur = q.pop(0)
            # print("bfs at", cur)
            currchar = ord(lines[cur[0]][cur[1]])
            if currchar == 83:
                currchar = 97
            for d in dirs:
                new = [cur[0] + d[0], cur[1] + d[1]]
                # check inbounds
                if new[0] >= 0 and new[0] < len(lines) and new[1] >= 0 and new[1] < len(lines[0]):
                    otherchar = ord(lines[new[0]][new[1]])
                    if otherchar == 69:
                        otherchar = 122
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
print(len(starts))
count = 0
result = 10**9
for start in starts:
    count += 1
    if count % 500 == 0:
        print(count)
    # print(count)
    result = min(result, bfs(start, count))

print(bfs([4, 0], 0))
print(result)







