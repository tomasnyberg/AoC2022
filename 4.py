import sys
lines = list(map(str.strip, sys.stdin.readlines()))

intervals = []
for line in lines:
    split = line.split(",")
    intervals.append(list(map(lambda x: [int(y) for y in x.split("-")], split)))

p1res = 0
p2res = 0
for a, b in intervals:
    if (b[0] <= a[0] <= a[1] <= b[1]) or (a[0] <= b[0] <= b[1] <= a[1]):
        p1res += 1
    if (a[0] <= b[0] and b[0] <= a[1]) or (b[0] <= a[0] and a[0] <= b[1]):
        p2res += 1

print("Part one", p1res)
print("Part two", p2res)