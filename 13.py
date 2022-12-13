import sys, functools

def score(a, b):
    if type(a) == int and type(b) == int:
        return 0 if a == b else 1 if a < b else -1
    if type(a) == list and type(b) == list:
        for i in range(min(len(a), len(b))):
            if score(a[i], b[i]) != 0:
                return score(a[i], b[i])
        return 0 if len(a) == len(b) else 1 if len(a) < len(b) else -1
    return score(a, [b]) if type(a) == list else score([a], b) 

pkts = [list(map(eval, pair.split("\n"))) for pair in sys.stdin.read().split("\n\n")]
pkts = [item for sublist in pkts for item in sublist] + [[[2]], [[6]]]
p1res = sum((i//2) + 1 if score(pkts[i-1], pkts[i]) == 1 else 0 for i in range(1, len(pkts) - 2, 2))
pkts = sorted(pkts, key=functools.cmp_to_key(lambda a, b: -score(a, b)))
p2res = 1 * (pkts.index([[2]]) + 1) * (pkts.index([[6]]) + 1)

print("Part one:", p1res)
print("Part two:", p2res)