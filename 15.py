import sys,re
lines = list(map(str.strip, sys.stdin.readlines()))

sensors = {}
beacons = set()

row = 2000000
maxx = 0
maxy = 0
maxd = 0
minx = 0
miny= 0

# row = 10
for line in lines:
    x1, y1, x2, y2 = map(int, re.findall(r'-?\d+', line))
    d = abs(int(x1) - int(x2)) + abs(int(y1) - int(y2))
    sensors[(x1, y1)] = ((x2, y2), d)
    beacons.add((x2, y2))
    maxx = max(maxx, x1, x2)
    maxy = max(maxy, y1, y2)
    maxd = max(maxd, d)
    minx = min(minx, x1, x2)
    miny = min(miny, y1, y2)

print(maxx, maxy, minx, miny, maxd)
result = 0
for col in range(-5000000, 5000000):
    if col % 1000000 == 0:
        print(col)
    found = False
    if (row, col) in beacons:
        continue
    for s in sensors:
        closest = sensors[s][-1]
        # manhattan distance between (row, j) and s
        d = abs(col - s[0]) + abs(row - s[1])
        if d <= closest:
            found = True
            break
    if found:
        result += 1

print(result)

# guessed 6636384
# guessed 5175617

# should guess 4582668