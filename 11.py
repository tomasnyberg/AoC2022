import sys, re
monkeys = sys.stdin.read().split("\n\n")

monkey_list = []
for monkey in monkeys:
    _, starting, op, test, t, f = monkey.split("\n")
    starting = list(map(int, re.findall(r"\d+", starting)))
    op = op.split(" = ")[1].split(" ")[1:]
    test = int(test.split(" ")[-1])
    t = int(t.split(" ")[-1])
    f = int(f.split(" ")[-1])
    monkey_list.append((starting, op, test, t, f))

counts = [0]*len(monkey_list)
def cycle():
    for idx, m in enumerate(monkey_list):
        while m[0]:
            counts[idx] += 1
            item = m[0].pop(0) # fix
            second = int(m[1][1]) if m[1][1] != 'old' else item
            item = item * second if m[1][0] == '*' else item + second
            item //= 3
            if item % m[2] == 0:
                monkey_list[m[3]][0].append(item)
            else:
                # print(monkey_list[m[4]])
                monkey_list[m[4]][0].append(item)

for i in range(20):
    cycle()
counts.sort()
print(counts)
print(counts[-1] * counts[-2])