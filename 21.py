import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

adj_lists = {}
monkeys = {}
for line in lines:
    name, op = line.split(": ")
    monkeys[name] = int(op) if op[0].isdigit() else op
    adj_lists[name] = set([x for x in op.split() if x.isalpha()])

def topological_sort(adj_lists):
    visited = set()
    result = []
    def dfs(curr, result):
        visited.add(curr)
        for nbr in adj_lists[curr]:
            if nbr in visited:
                continue
            dfs(nbr, result)
        result.append(curr)
    for key in adj_lists:
        if key not in visited:
            dfs(key, result)
    return result

def attempt_eval(num, monkeys, part_two, topsort):
    monkeys['humn'] = num
    for name in [x for x in topsort if type(monkeys[x]) == str]:
        a, operation, b = monkeys[name].split()
        if part_two and name == 'root':
            return monkeys[a] >= monkeys[b]
        monkeys[name] = eval(str(monkeys[a]) + operation + str(monkeys[b]))
    return monkeys['root']

def bs():
    low = 0
    high = 10000000000000
    while low < high:
        mid = (low + high) >> 1
        res = attempt_eval(mid, monkeys.copy(), True, ts)
        if res:
            low = mid + 1
        else:
            high = mid
    return low - 1

ts = topological_sort(adj_lists)
res = attempt_eval(monkeys['humn'], monkeys.copy(), False, ts)

print("Part one:", math.floor(res))
print("Part two:", bs())
