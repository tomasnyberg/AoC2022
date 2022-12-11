import sys, re
from functools import reduce
whole_file = sys.stdin.read()
monkeys = whole_file.split("\n\n")

monkeylist = []
for monkey in monkeys:
    lines = monkey.split("\n")
    monkeylist.append([])
    monkeylist[-1].append(list(map(int,re.findall(r'\d+', lines[1]))))
    op = lines[2].split(": ")[1].split(" = ")[1].split(" ")[1:]
    monkeylist[-1].append(op)
    divby = int(re.findall(r'\d+', lines[3])[0])
    monkeylist[-1].append(divby)
    truethrow = int(re.findall(r'\d+', lines[4])[0])
    falsethrow = int(re.findall(r'\d+', lines[5])[0])
    monkeylist[-1].append(truethrow)
    monkeylist[-1].append(falsethrow)

divby = reduce(lambda x, y: x*y, reduce(lambda x, y: x+y, [i[0] for i in monkeylist]))
counts = [0 for i in range(len(monkeylist))]
def round():
    for m in range(len(monkeylist)):
        for i in range(len(monkeylist[m][0])):
            counts[m] += 1
            curr = monkeylist[m][0][i] % divby
            snd = int(monkeylist[m][1][1]) if monkeylist[m][1][1] != 'old' else curr
            curr = curr + snd if monkeylist[m][1][0] == "+" else curr * snd
            to_true, to_false = monkeylist[m][-2:]
            if curr % monkeylist[m][2] == 0:
                monkeylist[to_true][0].append(curr)
            else:
                monkeylist[to_false][0].append(curr)
        monkeylist[m][0] = []

for i in range(10000):
    if i % 1000 == 0:
        print(i)
        print(counts)
    round()
counts.sort()
print(counts[-1]*counts[-2])
