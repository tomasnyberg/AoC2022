import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

l, n = lines[0], len(lines[0])
print("Part one:", [i for i in range(4, n) if len(set(l[i-4:i])) == 4][0])
print("Part two:", [i for i in range(14, n) if len(set(l[i-14:i])) == 14][0])
