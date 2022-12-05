import sys, re
whole = sys.stdin.read()
cratepart, movelines = whole.split("\n\n")
crates = [[] for _ in range(len(re.findall("\d", cratepart.split("\n")[-1])))]
for line in cratepart.split("\n"):
    for i in range(1, len(line), 4):
        if 65 <= ord(line[i]) <= 90:
            crates[(i-1) // 4].append(line[i])
crates = [x[::-1] for x in crates]

def solve(part2, crates):
    for line in movelines.split("\n"):
        take, fr, to = list(map(int, re.findall("\d+", line)))
        takeboxes = crates[fr-1][-take:]
        if not part2: takeboxes = takeboxes[::-1]
        crates[fr-1] = crates[fr-1][:-take]
        crates[to-1] = crates[to-1] + takeboxes
    return ''.join([x[-1] for x in crates])
print("Part one:", solve(False, [x[:] for x in crates]))
print("Part two:", solve(True, [x[:] for x in crates]))
