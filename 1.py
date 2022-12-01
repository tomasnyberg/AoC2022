import sys
lines = list(map(str.strip, sys.stdin.readlines()))

result = 0
currtotal = 0
elves = []
for line in lines:
    if line == "":
        elves.append(currtotal)
        currtotal = 0
    else:
        currtotal+=int(line)
elves.append(currtotal)
elves.sort()

print("Part one:", elves[-1])
print("Part two:", sum(elves[-3:]))