import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

inputs = [(a, int(b)) for a, b in [line.split(" ") for line in lines]]
def movetail(tailpos, headpos):
    def movetoward(tailpos, headpos, dir):
        tailpos[dir] += 1 if headpos[dir] > tailpos[dir] else -1
    dist = abs(headpos[0] - tailpos[0]) + abs(headpos[1] - tailpos[1])
    if dist == 2:
        if headpos[0] != tailpos[0] and headpos[1] != tailpos[1]: return 
        dir = 1 if headpos[0] == tailpos[0] else 0
        movetoward(tailpos, headpos, dir)
    elif dist == 3 or dist == 4:
        movetoward(tailpos, headpos, 0)
        movetoward(tailpos, headpos, 1)

visitedp1 = set([(0, 0)])
visitedp2 = set([(0, 0)])
headpos = [0, 0]
tailposes = [[0, 0] for _ in range(9)]
mapped = {'U': (0, 1), 'D': (0, -1), 'R': (1, 1), 'L': (1, -1)}
for d, amount in inputs:
    for _ in range(amount):
        idx, add = mapped[d]
        headpos[idx] += add
        movetail(tailposes[-1], headpos)
        for i in range(len(tailposes) - 1, 0, -1):
            movetail(tailposes[i-1], tailposes[i])
        visitedp2.add(tuple(tailposes[0]))
        visitedp1.add(tuple(tailposes[-1]))
print("Part one:", len(visitedp1))
print("Part two:", len(visitedp2))
