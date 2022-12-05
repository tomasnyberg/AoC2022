import sys
lines = list(map(str.strip, sys.stdin.readlines()))
crates = [
['S', 'P', 'W', 'N', 'J', 'Z'],
['T', 'S', 'G'],
['H', 'L', 'R', 'Q', 'V'],
['D', 'T', 'S', 'V'],
['J',' M', 'B', 'D', 'T', 'Z', 'Q'],
['L', 'Z', 'C', 'D', 'J', 'T', 'W', 'M'],
['J','T', 'G', 'W', 'M', 'P', 'L'],
['H','Q','F','B','T','M','G','N'],
['W','Q','B','P','C','G','D','R']]
# crates = [
#     ['N', 'Z'],
#     ['D', 'C', 'M'],
#     ['P']
# ]
for x in crates:
    x.reverse()
for x in crates:
    print(x)
moves = []
for line in lines:
    if line and line[0] == "m":
        split = (line.split(" "))
        take = int(split[1])
        fr = int(split[3])
        to = int(split[5])
        print("moving", take, "from", fr, "to", to)
        for _ in range(take):
            taken = crates[fr - 1].pop()
            crates[to - 1].append(taken)

for x in crates:
    print(x[-1], end="")
print()