import sys,re
lines = list(map(str.strip, sys.stdin.readlines()))

def manhattan(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])
scanners = {}
beacons = set()
for line in lines:
    a, b, c, d = map(int, re.findall(r'-?\d+', line))
    scanners[(a, b)] = manhattan((a, b), (c, d))
    beacons.add((c, d))

def part_one():
    row = 2000000
    result = 0
    for x in range(-5000000, 5000000):
        if (x, row) in scanners or (x, row) in beacons: continue
        if any(manhattan((x, row), (a, b)) <= d for (a, b), d in scanners.items()):
            result += 1
    return result

def part_two():
    # Get all the lines of the diamond surrounding a scanner.
    uplines, downlines = set(), set()
    for((x,y), d) in scanners.items():
        uplines |= set([y-x+d+1, y-x-d-1])
        downlines |= set([y+x+d+1,y+x-d-1])
    bound = 4000000
    # For every line going up and down, find where they intersect.
    # If all the scanners are further away from the intersection than their distance
    # to their nearest scanner, that is our answer.
    for up in uplines:
        for down in downlines:
            intersect = ((down-up)//2, (down + up)//2)
            if all(0 < c < bound for c in intersect):
                if all(manhattan(intersect, (x, y)) > d for (x, y), d in scanners.items()):
                    return (bound*intersect[0] + intersect[1])

print("Part one:", part_one())
print("Part two:", part_two())