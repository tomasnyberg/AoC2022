import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# ###C index 0

# .#.
# #C# index 1
# .#.

# ..#
# ..#
# ##C index 2

# #
# #
# #
# C index 3
# 
# ##
# #C index 4

dirs = lines[0]*1000
print(len(dirs))

# 7 units wide, 100 tall grid
grid = [[0 for _ in range(7)] for _ in range(100)]
for xs in (grid[-5:]):
    print(xs)

def check_down(i, center):
# index 0 doesn't draw properly
# index 1 doesn't draw its sides
# index 4 doesn't draw at all
    row, col = center
    if i == 0:
        if row < len(grid) - 1 and all(grid[row+1][newcol] == 0 for newcol in range(col-3, col+1)):
            return [row+1, col]
        else:
            for newcol in range(col-3, col+1):
                grid[row][newcol] = 1 
            return [row, col]
    elif i == 1:
        if row < len(grid) - 2 and grid[row+1][col+1] == 0 and grid[row+1][col-1] == 0 and grid[row+2][col] == 0:
            return [row+1, col] 
        else:
            grid[row][col] = 1
            grid[row][col+1] = 1
            grid[row][col-1] = 1
            grid[row-1][col] = 1
            grid[row+1][col] = 1
            return [row, col]
    elif i == 2:
        if row < len(grid) - 1 and all(grid[row+1][newcol] == 0 for newcol in range(col-2, col+1)):
            return [row+1, col]
        else:
            for newcol in range(col-2, col+1):
                grid[row][newcol] = 1
            grid[row-1][col] = 1
            grid[row-2][col] = 1
            return [row, col]
    elif i == 3:
        if row < len(grid) - 1 and grid[row+1][col] == 0:
            return [row+1, col]
        else:
            for newrow in range(row-3, row+1):
                grid[newrow][col] = 1
            return [row, col]
    elif i == 4:
        if row < len(grid) - 1 and grid[row+1][col] == 0 and grid[row+1][col-1] == 0:
            return [row+1, col]
        else:
            print("4 landed at", row, col)
            grid[row][col] = 1
            grid[row][col-1] = 1
            grid[row-1][col-1] = 1
            grid[row-1][col] = 1
            return [row, col]
    else:
        print(i)
        raise Exception("Invalid i")
# Not 100% sure about these
startposes = {0: [0, 5], 1: [1,3], 3: [3, 2], 2:[2,4], 4:[1, 3]}

def print_grid():
    for row in grid[-15:]:
        print(''.join(['#' if x == 1 else '.' for x in row]))
    print("-------------")

for i in range(10):
    startpos = startposes[i % 5]
    print(startpos)
    while True:
        newpos = check_down(i%5, startpos)
        if newpos == startpos:
            print_grid()
            break
        else:
            startpos = newpos

