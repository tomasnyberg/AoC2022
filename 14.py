import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

matrix = set()
for line in lines:
    prev = None
    for x, y in (list(map(int, re.findall(r'\d+', s))) for s in line.split(" -> ")):
        if prev is not None:
            for i in range(min(prev[0], x), max(prev[0], x)+1):
                for j in range(min(prev[1], y), max(prev[1], y)+1):
                    matrix.add((j, i))
        prev = (x, y)

max_y = max(x for x, y in matrix) + 2
for i in range(50000):
    matrix.add((max_y, i))

def sand():
    p = [0, 500]
    if tuple(p) in matrix: return True
    while p[0] < 999:
        broken = False
        for dj in [0, -1, 1]:
            if (p[0]+1, p[1]+dj) not in matrix:
                p[0]+=1
                p[1]+=dj
                broken = True
                break
        if broken: 
            continue
        matrix.add(tuple(p))
        return False

def solve():
    for i in range(100000):
        if sand():
            return i

print("Part two:", solve())
