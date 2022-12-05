import sys, re
whole = sys.stdin.read()
cratepart, movelines = whole.split("\n\n")
crates = [[] for _ in range(len(re.findall("\d", cratepart.split("\n")[-1])))]
for line in cratepart.split("\n"):
    for i in range(1, len(line), 4):
        if 65 <= ord(line[i]) <= 90:
            crates[(i-1) // 4].append(line[i])
for x in crates:
    x.reverse()

def solve(part2, crates):
    for line in movelines.split("\n"):
        if line and line[0] == "m":
            split = (line.split(" "))
            take = int(split[1])
            fr = int(split[3])
            to = int(split[5])
            if part2:
                takeboxes = crates[fr-1][-take:]
                for _ in range(take):
                    crates[fr-1].pop()
                for x in takeboxes:
                    crates[to-1].append(x)
            else:
                for _ in range(take):
                    taken = crates[fr - 1].pop()
                    crates[to - 1].append(taken)
    return ''.join([x[-1] for x in crates])

# Create a copy of the crates array
print("Part one:", solve(False, [x[:] for x in crates]))
print("Part two:", solve(True, [x[:] for x in crates]))
