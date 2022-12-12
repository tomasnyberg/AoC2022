import sys, re
monkeys = sys.stdin.read().split("\n\n")

monkey_list = []
MOD = 1
for monkey in monkeys:
    _, starting, op, test, t, f = monkey.split("\n")
    starting = list(map(int, re.findall(r"\d+", starting)))
    op = op.split(" = ")[1].split(" ")[1:]
    test, t, f = map(lambda x: int(x.split(" ")[-1]), [test, t, f])
    MOD *= test
    monkey_list.append((starting, op, test, t, f))

def solve(iterations, part_two):
    def cycle(counts, monkey_list, part_two=False):
        for idx, m in enumerate(monkey_list):
            while m[0]:
                counts[idx] += 1
                item = m[0].pop()
                second = int(m[1][1]) if m[1][1] != 'old' else item
                item = item * second if m[1][0] == '*' else item + second
                item = item % MOD if part_two else item // 3
                monkey_list[m[3 if item % m[2] == 0 else 4]][0].append(item)
    monkeys = [(list([x for x in m[0]]), m[1], m[2], m[3], m[4]) for m in monkey_list]
    counts = [0]*len(monkey_list)
    for _ in range(iterations):
        cycle(counts, monkeys, part_two)
    counts.sort()
    return counts[-1] * counts[-2]

print("Part one:", solve(20, False))
print("Part two:", solve(10000, True))