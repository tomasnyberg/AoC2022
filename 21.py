import sys
lines = list(map(str.strip, sys.stdin.readlines()))

known = {}
unknown = {}
for line in lines:
    name, op = line.split(": ")
    if op[0].isdigit():
        known[name] = int(op)
    else:
        unknown[name] = op

def attempt_eval(num, known, unknown, part_two):
    known['humn'] = num
    while True:
        to_del = []
        for name, val in unknown.items():
            a, operation, b = val.split()
            if a in known and b in known:
                if name == 'root' and part_two:
                    return known[a] >= known[b]
                a = str(known[a])
                b = str(known[b])
                known[name] = eval(a + operation + b)
                to_del.append(name)
            else:
                continue
        if not to_del:
            break
        for name in to_del:
            del unknown[name]
    return known['root']
    
def bs():
    low = 0
    high = 10000000000000
    while low < high:
        mid = (low + high) // 2
        res = attempt_eval(mid, known.copy(), unknown.copy(), True)
        if res:
            low = mid + 1
        else:
            high = mid
    return low - 1

print(bs())
