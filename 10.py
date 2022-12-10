import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))
grid = [["." for _ in range(40)] for _ in range(6)]

def solve():
    total = [0]
    iterations = [0]
    countset = set([20, 60, 100, 140, 180, 220])
    x = 1
    for line in lines:
        def cpu():
            iterations[0] += 1
            if iterations[0] in countset:
                total[0] += x*iterations[0]
            distance = abs((iterations[0] - 1)%40-x)
            grid[(iterations[0]-1)//40][(iterations[0]-1)%40] = ["#","."][distance >= 2]
        if line[0] == 'a':
            add = int(line.split(" ")[1])
            [cpu() for _ in range(2)]
            x += add
        else:
            cpu()
    return total

print("Part one:", solve()[0])
print("Part two:")
for xs in grid:
    for x in xs:
        if x == "#":
            print(x, end="")
        else:
            print(" ", end="")
    print()

