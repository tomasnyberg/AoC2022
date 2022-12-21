import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

def topological_sort(n, adj_lists):
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

adj_lists = {}

known = {}
unknown = {}
for line in lines:
    name, op = line.split(": ")
    if op[0].isdigit():
        known[name] = int(op)
        adj_lists[name] = set()
    else:
        unknown[name] = op
        adj_lists[name] = set([x for x in op.split() if x.isalpha()])

def attempt_eval(num, known, unknown, part_two, topsort):
    known['humn'] = num
    for name in topsort:
        if name in known:
            continue
        a, operation, b = unknown[name].split()
        if part_two and name == 'root':
            return known[a] >= known[b]
        a = str(known[a])
        b = str(known[b])
        known[name] = eval(a + operation + b)
    return known['root']

def bs():
    low = 0
    high = 10000000000000
    while low < high:
        mid = (low + high) // 2
        res = attempt_eval(mid, known.copy(), unknown.copy(), True, ts)
        if res:
            low = mid + 1
        else:
            high = mid
    return low - 1

res = attempt_eval(known['humn'], known.copy(), unknown.copy(), False, topological_sort(len(adj_lists), adj_lists))
ts = topological_sort(len(adj_lists), adj_lists)

print("Part one:", math.floor(res))
print("Part two:", bs())
