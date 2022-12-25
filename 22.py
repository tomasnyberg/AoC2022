import sys, re
lines = list(sys.stdin.readlines())

instructions = lines[-1]
lines = lines[:-2]

def findnext(direction, pos):
    row, col = pos
    di, dj = direction
    count = 0
    while count == 0 or lines[row][col] == ' ':
        count += 1
        row += di
        col += dj
        if row >= len(lines):
            row = 0
        if col >= len(lines[row]):
            col = 0
        if row < 0:
            row = len(lines) - 1
        if col < 0:
            col = len(lines[row]) - 1
    return [row, col]

def move(num, direction, pos):
    i = 0
    while i < num:
        newrow = pos[0] + direction[0]
        newcol = pos[1] + direction[1]
        if not (0 <= newrow < len(lines)) or not 0 <= newcol < len(lines[newrow]) or lines[newrow][newcol] == ' ':
            newrow, newcol = findnext(direction, pos)
            if lines[newrow][newcol] == '#':
                return pos, direction
            pos = [newrow, newcol]
            continue
        if lines[newrow][newcol] == '#':
            return pos, direction
        pos = [newrow, newcol]
        i+=1
    return pos, direction

def wrap(pos, dir):
    x, y = pos
    if dir == [0, 1] and x//50 == 0: return [149-x, 99], [0, -1]
    if dir == [0, 1] and x//50 == 1: return [ 49,x+ 50], [-1, 0]
    if dir == [0, 1] and x//50 == 2: return [149-x,149], [0, -1]
    if dir == [0, 1] and x//50 == 3: return [149,x-100], [-1, 0]
    if dir == [0, -1] and x//50 == 0: return [149-x,  0], [0, 1]
    if dir == [0, -1] and x//50 == 1: return [100,x- 50], [1, 0]
    if dir == [0, -1] and x//50 == 2: return [149-x, 50], [0, 1]
    if dir == [0, -1] and x//50 == 3: return [  0,x-100], [1, 0]
    if dir == [1, 0] and y//50 == 0: return [  0,y+100], [1, 0]
    if dir == [1, 0] and y//50 == 1: return [100+y, 49], [0, -1]
    if dir == [1, 0] and y//50 == 2: return [-50+y, 99], [0, -1]
    if dir == [-1, 0] and y//50 == 0: return [ 50+y, 50], [0, 1]
    if dir == [-1, 0] and y//50 == 1: return [100+y,  0], [0, 1]
    if dir == [-1, 0] and y//50 == 2: return [199,y-100], [-1, 0]
    assert False

grid = {}
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] in '#.':
            grid[(i, j)] = lines[i][j]

def move3d(num, direction, pos):
    for _ in range(num):
        p, d = (pos[0] + direction[0], pos[1] + direction[1]), direction
        if p not in grid:
            p, d = wrap(p, d)
        p = tuple(p)
        if grid[p] == '.': pos, direction = p, d
    return pos, direction

d1, d2 = [0, 1], [0,1]
p1, p2 = (0, 50), (0, 50)
i = 0
for x in re.findall(r'[LR]|\d+', instructions):
    if x == 'R':
        d1 = [d1[1], -d1[0]]
        d2 = [d2[1], -d2[0]]
    elif x == 'L':
        d1 = [-d1[1], d1[0]]
        d2 = [-d2[1], d2[0]]
    else:
        p1, d1 = move(int(x), d1, p1)
        p2, d2 = move3d(int(x), d2, p2)

def score(direction, pos):
    facingscore = [[0, 1], [1, 0], [0, -1], [-1, 0]].index(direction)
    print(1000*(pos[0]+1) + 4*(pos[1]+1) + facingscore)

score(d1, p1)
score(d2, p2)
