import sys,re
lines = list(map(str.strip, sys.stdin.readlines()))

sensors = {}
beacons = set()

row = 2000000

# row = 10
for line in lines:
    y1, x1, y2, x2 = map(int, re.findall(r'-?\d+', line))
    d = abs(int(x1) - int(x2)) + abs(int(y1) - int(y2))
    sensors[(x1, y1)] = ((x2, y2), d)
    beacons.add((x2, y2))
# for r, c in sensors:
#     print(r, c)
result = 0
for col in range(-5000000, 5000000):
    if col % 1000000 == 0:
        print(col)
    found = False
    if (row, col) in beacons or ( row, col) in sensors:
        continue
    for s in sensors:
        closest = sensors[s][-1]
        d = abs(col - s[1]) + abs(row - s[0])
        if d <= closest:
            found = True
            break
    if found:
        print(row, col)
        result += 1
print(result)





# guessed 6636384
# guessed 5175617
# guessed 4582668