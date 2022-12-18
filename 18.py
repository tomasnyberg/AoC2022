import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

# 100 by 100 by 100 grid
grid = [[[0 for k in range(100)] for j in range(100)] for i in range(100)]
# All dirs in 6 directions
dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
coordinates = []
for line in lines:
    a, b, c = map(int, re.findall(r'-?\d+', line))
    coordinates.append((a,b,c))
    grid[a][b][c] = 1
result = 0
for x, y, z in coordinates:
    for i, j, k in dirs:
        if grid[x+i][y+j][z+k] == 0:
            result += 1
print(result)