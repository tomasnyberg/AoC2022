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
# for col in range(0, 4000000):
#     if col % 1000000 == 0:
#         print(col)
#     found = False
#     if (row, col) in beacons or ( row, col) in sensors:
#         continue
#     for s in sensors:
#         closest = sensors[s][-1]
#         d = abs(col - s[1]) + abs(row - s[0])
#         if d <= closest:
#             found = True
#             break
#     if found:
#         print(row, col)
#         result += 1
MAX = 4000000
def solve():
    def check(pos):
        row, col = pos
        if row > MAX or col > MAX or row < 0 or col < 0:
            return False
        # Check if every sensor is further away than its beacon
        for s in sensors:
            r, c, d =  s[0], s[1], sensors[s][-1]
            if abs(row - r) + abs(col - c) <= d:
                return False
        return True
    for s in sensors:
        # print(s)
        r, c, d =  s[0], s[1], sensors[s][-1]
        # r,c,d = 0,0,1
        pos = [r - d - 1, c]
        visited = set()
        # print(1)
        while pos[0] < r:
            if(check(pos)):
                print(pos)
            # print(pos)
            pos[0] += 1
            pos[1] += 1
            visited.add((pos[0], pos[1]))
        # print(2)
        while pos[1] > c:
            if(check(pos)):
                print(pos)
            # print(pos)
            pos[0] += 1
            pos[1] -= 1
            visited.add((pos[0], pos[1]))
        # print(3)
        while pos[0] > r:
            if(check(pos)):
                print(pos)
            # print(pos)
            pos[0] -= 1
            pos[1] -= 1
            visited.add((pos[0], pos[1]))
        # print(4)
        while pos[1] <= c:
            if(check(pos)):
                print(pos)
            # print(pos)
            pos[0] -= 1
            pos[1] += 1
            visited.add((pos[0], pos[1]))

solve()
print(result)