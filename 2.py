import sys
lines = list(map(str.strip, sys.stdin.readlines()))

p1 = 0
p2 = 0
p1d = {'A X': 4, 'B X': 1, 'C X': 7, 'A Y': 8, 'B Y': 5, 'C Y': 2, 'A Z': 3, 'B Z': 9, 'C Z': 6}
p2d = {'A X': 3, 'B X': 1, 'C X': 2, 'A Y': 4, 'B Y': 5, 'C Y': 6, 'A Z': 8, 'B Z': 9, 'C Z': 7}
for line in lines:
    p1 += p1d[line]
    p2 += p2d[line]

print("Part one:", p1)
print("Part two:", p2)