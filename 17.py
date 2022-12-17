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
grid = [[0 for _ in range(7)] for _ in range(100000)]
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

def check_side(i, center, dir):
    row, col = center
    if i == 0:
        if dir == '<':
            if col - 3 > 0 and grid[row][col-4] == 0:
                return [row, col-1]
            else:
                return [row, col]
        elif dir == '>':
            if col + 1 < len(grid[0]) and grid[row][col+1] == 0:
                return [row, col+1]
            else:
                return [row, col]
    elif i == 1:
        if dir == '<':
            if col - 1 > 0 and grid[row][col-2] == 0 and grid[row+1][col-1] == 0 and grid[row-1][col-1] == 0:
                return [row, col-1]
            else:
                return [row, col]
        elif dir == '>':
            if col + 2 < len(grid[0]) and grid[row][col+2] == 0 and grid[row+1][col+1] == 0 and grid[row-1][col+1] == 0:
                return [row, col+1]
            else:
                return [row, col]
    elif i == 2:
        if dir == '<':
            if col - 2 > 0 and grid[row][col-3] == 0 and grid[row-1][col-1] == 0 and grid[row-2][col-1] == 0:
                return [row, col-1]
            else:
                return [row, col]
        elif dir == '>':
            if col + 1< len(grid[0]) and grid[row][col+1] == 0 and grid[row-1][col+1] == 0 and grid[row-2][col+1] == 0:
                return [row, col+1]
            else:
                return [row, col]
    elif i == 3:
        if dir == '<':
            # THIS LINE COULD BE WRONG
            if col - 1 > 0 and all(grid[newrow][col-1] == 0 for newrow in range(row-3, row+1)):
                return [row, col-1]
            else:
                return [row, col]
        elif dir == '>':
            if col + 1 < len(grid[0]) and all(grid[newrow][col+1] == 0 for newrow in range(row-3, row+1)):
                return [row, col+1]
            else:
                return [row, col]
    elif i == 4:
        if dir == '<':
            if col - 1 > 0 and grid[row][col-2] == 0 and grid[row-1][col-2] == 0:
                return [row, col-1]
            else:
                return [row, col]
        elif dir == '>':
            if col + 1 < len(grid[0]) and grid[row][col+1] == 0 and grid[row-1][col+1] == 0:
                return [row, col+1]
            else:
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

highest = len(grid)
diridx = 0
for i in range(2022):
    startpos = startposes[i % 5]
    startpos[0] = highest - 4
    if i % 5 == 1:
        startpos[0] -= 1
    while True:
        # print(startpos, "asdlfk")
        startpos = check_side(i%5, startpos, dirs[diridx])
        diridx+=1
        diridx %= len(dirs)
        newpos = check_down(i%5, startpos)
        if newpos == startpos:
            imodded = i % 5
            if imodded == 0:
                highest = min(highest, startpos[0])
            elif imodded == 1 or imodded == 4:
                highest = min(highest, startpos[0] - 1)
            elif imodded == 2:
                highest = min(highest, startpos[0] - 2)
            elif imodded == 3:
                highest = min(highest, startpos[0] - 3)
            # print_grid()
            break
        else:
            startpos = newpos
print(len(grid) - highest)

# guessed 3272, too high

