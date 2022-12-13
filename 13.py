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
p1res = 0
all_packets = [[[2]], [[6]]]
for j in range(len(pairs)):
    pair = list(map(eval, pairs[j].split("\n")))
    all_packets += pair
    if score(pair[0], pair[1]) == 1:
        p1res += j + 1

all_packets = sorted(all_packets, key=functools.cmp_to_key(lambda a, b: -score(a, b)))
res = 1 * (all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)
print("Part one:", p1res)
print("Part two:", res)