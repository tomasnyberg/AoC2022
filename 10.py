import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))
grid = [["." for _ in range(40)] for _ in range(6)]

total = 0
iterations = 0
countset = set([20, 60, 100, 140, 180, 220])
x = 1
for line in lines:
    def between_iterations():
        distance = abs((iterations - 1)%40-x)
        grid[(iterations-1)//40][(iterations-1)%40] = ["#","."][distance >= 2]
        if iterations in countset:
            return x*iterations
        return 0
    if line[0] == 'a':
        for _ in range(2):
            iterations += 1
            total += between_iterations()
        x += int(line.split(" ")[1])
    else:
        iterations +=1
        total += between_iterations()

print("Part one:", total)
print("Part two:")
for xs in grid:
    [print(chr(0x2588) if x == "#" else " ", end="") for x in xs]
    print()
