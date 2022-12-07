import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

dirs = {}
dirstack = ["/"]
for line in lines[2:]:
    # print(dirs, dirstack)
    if line[0] == '$':
        split = line.split(" ")
        if len(split) == 3:
            goto = split[2]
            if goto == "..":
                dirstack.pop()
            else:
                dirstack.append(goto)
    elif line[0] == "d":
        split = line.split(" ")
        for d in dirs:
            if d not in dirs:
                dirs[d] = [0, []]
            dirs[d][1].append(split[1])
    else:
        split = line.split(" ")
        for d in dirstack:
            if d not in dirs:
                dirs[d] = [0, []]
            dirs[d][0] += int(split[0])
result = 0
for d in dirs:
    if dirs[d][0] <= 100000:
        result += dirs[d][0]
print(result)


