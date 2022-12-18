import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

coordinates = set()
for line in lines:
    x, y, z = map(int, re.findall(r'-?\d+', line))
    coordinates.add((x, y, z))

dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
result = 0
for x, y, z in coordinates:
    for dx, dy, dz in dirs:
        if (x + dx, y + dy, z + dz) not in coordinates:
            result += 1
            
visited = set()
result2 = set()
q = [(0, 0, 0)]
while q:
    x, y, z = q.pop()
    visited.add((x, y, z))
    for dx, dy, dz in dirs:
        if not (-5 <= x + dx <= 30 and -5 <= y + dy <= 30 and -5 <= z + dz <= 30):
            continue
        if (x + dx, y + dy, z + dz) in coordinates:
            result2.add((x,y,z,x + dx, y + dy, z + dz))
        elif (x + dx, y + dy, z + dz) not in visited:
            q.append((x + dx, y + dy, z + dz))

print("Part one:", result)
print("Part two:", len(result2))
