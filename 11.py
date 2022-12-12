import sys, re
from queue import deque
monkeys = sys.stdin.read().split("\n\n")

monkey_list = []
MOD = 1
for monkey in monkeys:
    _, starting, op, test, t, f = monkey.split("\n")
    starting = deque(map(int, re.findall(r"\d+", starting)))
    op = op.split(" = ")[1].split(" ")[1:]
    test = int(test.split(" ")[-1])
    MOD *= test
    t = int(t.split(" ")[-1])
    f = int(f.split(" ")[-1])
    monkey_list.append((starting, op, test, t, f))

def cycle(counts, monkey_list, part_two=False):
    for idx, m in enumerate(monkey_list):
        while m[0]:
            counts[idx] += 1
            item = m[0].popleft()
            second = int(m[1][1]) if m[1][1] != 'old' else item
            item = item * second if m[1][0] == '*' else item + second
            item = item % MOD if part_two else item // 3
            if item % m[2] == 0:
                monkey_list[m[3]][0].append(item)
            else:
                monkey_list[m[4]][0].append(item)

def solve(iterations, part_two):
    monkeys = [(deque([x for x in m[0]]), m[1], m[2], m[3], m[4]) for m in monkey_list]
    counts = [0]*len(monkey_list)
    for i in range(iterations):
        cycle(counts, monkeys, part_two)
    counts.sort()
    return counts[-1] * counts[-2]

print("Part one:", solve(20, False))
print("Part two:", solve(10000, True))