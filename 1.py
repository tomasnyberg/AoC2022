import sys
elfsplit = sys.stdin.read().split("\n\n")
doublesplit = (list(map(lambda x: x.split("\n"), elfsplit)))
elves = list(map(sum, map(lambda xs: [int(x) for x in xs], doublesplit)))

print("Part one:", max(elves))
print("Part two:", sum(sorted(elves)[-3:]))
