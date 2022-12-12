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

def cycle(counts, part_two=False):
    for idx, m in enumerate(monkey_list):
        while m[0]:
            counts[idx] += 1
            item = m[0].popleft()
            second = int(m[1][1]) if m[1][1] != 'old' else item
            item = item * second if m[1][0] == '*' else item + second
            if part_two:
                item %= MOD
            else:
                item //= 3
            if item % m[2] == 0:
                monkey_list[m[3]][0].append(item)
            else:
                # print(monkey_list[m[4]])
                monkey_list[m[4]][0].append(item)

def biggest_two(counts):
    counts.sort()
    return counts[-1] * counts[-2]

def part_one():
    counts = [0]*len(monkey_list)
    for i in range(20):
        cycle(counts, False)
    return biggest_two(counts)

def part_two():
    counts = [0]*len(monkey_list)
    for i in range(10000):
        cycle(counts, True)
    return biggest_two(counts)

# print(part_one())
print(part_two())