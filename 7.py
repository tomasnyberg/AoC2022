import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

dirs = {}
stack = ["$"]
for line in lines[2:]:
    split = line.split(" ")
    if line[0] == '$':
        if split[1] == 'ls': continue
        if split[2] == '..':
            stack.pop()
        else:
            stack.append(split[2])
    # elif line[0] == 'd':
    elif line[0].isdigit():
        stackcopy = stack[:]
        while stackcopy:
            d = "/".join(stackcopy)
            dirs[d] = dirs.get(d, 0) + int(line.split(" ")[0])
            stackcopy.pop()
total = 0
result = 0
for d in dirs:
    total += dirs[d]
    if dirs[d] <= 100000:
        result += dirs[d]
print("Part one:", result)
required = 30000000 - (70000000 - dirs["$"])
candidates = []
for d in dirs:
    if dirs[d] >= required:
        candidates.append(dirs[d])
print("Part two:", min(candidates))






