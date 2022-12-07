import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

dirs = {}
stack = ["$"]
for line in list(filter(lambda x: x != '$ ls', lines))[2:]:
    split = line.split(" ")
    if line[0] == '$':
        stack = stack[:-1] if split[2] == '..' else stack + [split[2]]
    elif line[0].isdigit():
        stackcopy = stack[:]
        while stackcopy:
            d = "/".join(stackcopy)
            dirs[d] = dirs.get(d, 0) + int(line.split(" ")[0])
            stackcopy.pop()
            
required = 30000000 - (70000000 - dirs["$"])
print("Part one:", sum([dirs[d] for d in dirs if dirs[d] <= 100000]))
print("Part two:", min([dirs[d] for d in dirs if dirs[d] >= required]))
