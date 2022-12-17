import sys
lines = list(map(str.strip, sys.stdin.readlines()))

dirs = lines[0]
def generate_pieces(i, row):
    if i == 0:
        return set([(2,row), (3,row), (4,row), (5,row)])
    elif i == 1:
        return set([(3,row), (3,row-1), (3, row-2), (2, row-1), (4, row-1)])
    elif i == 2:
        return set([(2,row), (3,row), (4,row), (4, row-1), (4, row-2)])
    elif i == 3:
        return set([(2,row), (2,row-1), (2,row-2), (2,row-3)])
    elif i == 4:
        return set([(2,row), (3,row), (2,row-1), (3,row-1)])
    else:
        assert(False)

grid = [[0 for _ in range(7)] for _ in range(5000)]

def move_down(piece):
    if all(y+1 < len(grid) for x, y in piece) and all(grid[y+1][x] == 0 or (x, y+1) in piece for x, y in piece):
        return [True, set((x, y+1) for x, y in piece)]
    else:
        for x, y in piece:
            grid[y][x] = 1
        return [False, piece]

def move_side(piece, dir):
    dx = 1 if dir == ">" else -1
    if all(0 <= x+dx < len(grid[0]) for x, y in piece) and all(grid[y][x+dx] == 0 or (x+dx, y) in piece for x, y in piece):
        return set((x+dx, y) for x, y in piece)
    else:
        return piece

def signature(streamidx, rockidx, grid, height):
    return (streamidx, rockidx, tuple(tuple(xs) for xs in grid[height:height+10]))

def find_first():
    heights = []
    seen = {}
    highest = len(grid)
    idx = 0
    additional = 0
    i = 0
    added = False
    actual = 0
    while i < 1000000000000:
        piece = generate_pieces(i%5, highest - 4)
        while piece:
            dir = dirs[idx]
            idx = (idx + 1) % len(dirs)
            piece = move_side(piece, dir)
            good, piece = move_down(piece)
            if not good:
                highest = min(highest, min(y for x, y in piece))
                heights.append(highest)
                if not added:
                    sig = signature(idx, i%5, grid, highest)
                    if sig in seen:
                        additional = ((1000000000000 - i) // (i - seen[sig][1])) * (seen[sig][0] - highest)
                        i += ((1000000000000 - i) // (i - seen[sig][1])) * (i - seen[sig][1])
                        added = True
                    seen[sig] = (highest, i)
                break
        i += 1
        actual += 1
        if actual == 2022:
            print("Part one:", len(grid) - highest)
    print("Part two:", additional+ len(grid) - highest)

find_first()
