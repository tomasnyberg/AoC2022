import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

# 100 by 100 by 100 grid
grid = [[[0 for k in range(100)] for j in range(100)] for i in range(100)]
# All dirs in 6 directions
dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
coordinates = set()
for line in lines:
    a, b, c = map(int, re.findall(r'-?\d+', line))
    coordinates.add((a,b,c))
    grid[a][b][c] = 1
result = 0
for x, y, z in coordinates:
    result += 6
    for dx, dy, dz in dirs:
        if grid[x+dx][y+dy][z+dz] == 1:
            result -=1 
every = set((x,y,z) for x in range(100) for y in range(100) for z in range(100))
empty = every - coordinates
def bfs():
    q = [(0,0,0)]
    while q:
        c = q.pop()
        if c in empty:
            empty.remove(c)
            q.extend([(c[0]+dx, c[1]+dy, c[2]+dz) for dx, dy, dz in dirs])
bfs()
for c in empty:
    result += 6
    for dx, dy, dz in dirs:
        newcoords = (c[0]+dx, c[1]+dy, c[2]+dz)
        if newcoords in coordinates:
            result -= 2
    coordinates.add(c)
            
print(result)