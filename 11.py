import sys, re
whole_file = sys.stdin.read()
monkeys = whole_file.split("\n\n")

monkeylist = []
for monkey in monkeys:
    lines = monkey.split("\n")
    monkeylist.append([])
    starting = lines[1]
    # convert this into only numbers Starting items: 76, 66, 74, 87, 70, 56, 51, 66
    starting = list(map(int,re.findall(r'\d+', starting)))
    monkeylist[-1].append(starting)
    op = lines[2].split(": ")[1].split(" = ")[1].split(" ")[1:]
    monkeylist[-1].append(op)
    divby = int(re.findall(r'\d+', lines[3])[0])
    monkeylist[-1].append(divby)
    truethrow = int(re.findall(r'\d+', lines[4])[0])
    falsethrow = int(re.findall(r'\d+', lines[5])[0])
    monkeylist[-1].append(truethrow)
    monkeylist[-1].append(falsethrow)

gcd = 1
for i in range(len(monkeylist)):
    for j in range(len(monkeylist[i][0])):
        gcd *= monkeylist[i][0][j]

counts = [0 for i in range(len(monkeylist))]
def round():
    for m in range(len(monkeylist)):
        for i in range(len(monkeylist[m][0])):
            counts[m] += 1
            curr = monkeylist[m][0][i] % gcd
            if monkeylist[m][1][0] == "+":
                if monkeylist[m][1][1] == 'old':
                    curr += curr
                else:
                    curr += int(monkeylist[m][1][1])
            elif monkeylist[m][1][0] == "*":
                if monkeylist[m][1][1] == 'old':
                    curr *= curr
                else:
                    curr *= int(monkeylist[m][1][1])
            else:
                print("invalid state", monkeylist[m], i, curr)
                return
            toiftrue = monkeylist[m][3]
            toiffalse = monkeylist[m][4]
            if curr % monkeylist[m][2] == 0:
                monkeylist[toiftrue][0].append(curr)
            else:
                monkeylist[toiffalse][0].append(curr)
        monkeylist[m][0] = []

for i in range(10000):
    if i % 1000 == 0:
        print(i)
        print(counts)
    round()
counts.sort()
print(counts[-1]*counts[-2])
