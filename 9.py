import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

inputs = []
for line in lines:
    a, b = line.split(" ")
    inputs.append([a, int(b)])

def movetail(tailpos, headpos):
    def movetoward(tailpos, headpos, dir):
        tailpos[dir] += 1 if headpos[dir] > tailpos[dir] else -1
    dist = abs(headpos[0] - tailpos[0]) + abs(headpos[1] - tailpos[1])
    if dist == 2:
        if headpos[0] != tailpos[0] and headpos[1] != tailpos[1]: return 
        dir = 1 if headpos[0] == tailpos[0] else 0
        movetoward(tailpos, headpos, dir)
    elif dist == 3:
        dir = 0 if headpos[0] > tailpos[0] else 1
        movetoward(tailpos, headpos, dir)
        movetoward(tailpos, headpos, 1 - dir)
    elif dist == 4:
        movetoward(tailpos, headpos, 0)
        movetoward(tailpos, headpos, 1)

visited = set([(0, 0)])
headpos = [0, 0]
tailposes = []
for i in range(9):
    tailposes.append([0, 0])
for d, amount in inputs:
    # print(d, amount)
    for _ in range(amount):
        if d == 'U':
            headpos[0] += 1
        elif d == 'D':
            headpos[0] -= 1
        elif d == 'R':
            headpos[1] += 1
        else:
            headpos[1] -= 1
        movetail(tailposes[-1], headpos)
        for i in range(len(tailposes) - 1, 0, -1):
            movetail(tailposes[i-1], tailposes[i])
        visited.add(tuple(tailposes[0]))
print(len(visited))
