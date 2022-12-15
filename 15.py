import sys,re
lines = list(map(str.strip, sys.stdin.readlines()))

scanners = {}
def manhattan(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])
for line in lines:
    a, b, c, d = map(int, re.findall(r'-?\d+', line))
    scanners[(a, b)] = manhattan((a, b), (c, d))

uplines = set()
downlines = set()
for((x,y), d) in scanners.items():
    uplines.add(y-x+d+1)
    uplines.add(y-x-d-1)
    downlines.add(y+x+d+1)
    downlines.add(y+x-d-1)

bound = 4_000_000
for up in uplines:
    for down in downlines:
        intersect = ((down-up)//2, (down + up)//2)
        if all(0 < c < bound for c in intersect):
            if all(manhattan(intersect, (x, y)) > d for (x, y), d in scanners.items()):
                print(bound*intersect[0] + intersect[1])
                break
