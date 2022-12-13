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

pairs = sys.stdin.read().split("\n\n")
all_packets = [list(map(eval, pair.split("\n"))) for pair in pairs]
all_packets = [item for sublist in all_packets for item in sublist] + [[[2]], [[6]]]
p1res = 0
for i in range(1, len(all_packets) - 2, 2):
    s = score(all_packets[i-1], all_packets[i])
    p1res += (i // 2) + 1 if s == 1 else 0
all_packets = sorted(all_packets, key=functools.cmp_to_key(lambda a, b: -score(a, b)))
res = 1 * (all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)

print("Part one:", p1res)
print("Part two:", res)