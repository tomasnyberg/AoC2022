import sys, re
monkey_list = sys.stdin.read().split("\n\n")

MOD = 1
for i in range(len(monkey_list)):
    _, starting, op, test, t, f = monkey_list[i].split("\n")
    starting = list(map(int, re.findall(r"\d+", starting)))
    op = op.split(" = ")[1].split(" ")[1:]
    test, t, f = map(lambda x: int(x.split(" ")[-1]), [test, t, f])
    MOD *= test
    monkey_list[i] = [starting, op, test, t, f]

def solve(iterations, part_two):
    def cycle(counts, monkey_list, part_two=False):
        for idx, m in enumerate(monkey_list):
            counts[idx] += len(m[0])
            for item in m[0]:
                second = int(m[1][1]) if m[1][1] != 'old' else item
                item = item * second if m[1][0] == '*' else item + second
                item = item % MOD if part_two else item // 3
                monkey_list[m[3 if item % m[2] == 0 else 4]][0].append(item)
            m[0] = []
    monkeys = [[list([x for x in m[0]]), m[1], m[2], m[3], m[4]] for m in monkey_list]
    counts = [0]*len(monkey_list)
    for _ in range(iterations):
        cycle(counts, monkeys, part_two)
    counts.sort()
    return counts[-1] * counts[-2]

print("Part one:", solve(20, False))
print("Part two:", solve(10000, True))