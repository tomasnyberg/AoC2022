import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

inputs = [(a, int(b)) for a, b in [line.split(" ") for line in lines]]

def movetail(tailpos, headpos):
    def movetoward(tailpos, headpos, dir):
        tailpos[dir] += 1 if headpos[dir] > tailpos[dir] else -1
    dist = abs(headpos[0] - tailpos[0]) + abs(headpos[1] - tailpos[1])
    if dist == 2:
        if headpos[0] != tailpos[0] and headpos[1] != tailpos[1]: return 
        movetoward(tailpos, headpos, 1 if headpos[0] == tailpos[0] else 0)
    elif dist == 3 or dist == 4:
        movetoward(tailpos, headpos, 0)
        movetoward(tailpos, headpos, 1)

visitedp1, visitedp2 = [set([(0, 0)]) for _ in range(2)]
snake = [[0, 0] for _ in range(10)]
directions = {'U': (0, 1), 'D': (0, -1), 'R': (1, 1), 'L': (1, -1)}
for direction, amount in inputs:
    for _ in range(amount):
        idx, add = directions[direction]
        snake[-1][idx] += add
        for i in range(len(snake)-1, 0, -1):
            movetail(snake[i-1], snake[i])
        visitedp1.add(tuple(snake[-2]))
        visitedp2.add(tuple(snake[0]))

print("Part one:", len(visitedp1))
print("Part two:", len(visitedp2))
