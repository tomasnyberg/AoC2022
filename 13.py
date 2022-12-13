import sys, re
import functools
pairs = sys.stdin.read().split("\n\n")
def score(a, b):
    if type(a) == int and type(b) == int:
        return 0 if a == b else 1 if a < b else -1
    if type(a) == list and type(b) == list:
        for i in range(min(len(a), len(b))):
            if score(a[i], b[i]) != 0:
                return score(a[i], b[i])
        return 0 if len(a) == len(b) else 1 if len(a) < len(b) else -1
    return score(a, [b]) if type(a) == list else score([a], b) 

result = 0
all_packets = [[[2]], [[6]]]
for j in range(len(pairs)):
    pair = pairs[j]
    pair = pair.split("\n")
    a = pair[0]
    b = pair[1]
    a = eval(a)
    b = eval(b)
    all_packets.append(a)
    all_packets.append(b)
    if score(a, b) == 1:
        result += j + 1

all_packets = sorted(all_packets, key=functools.cmp_to_key(lambda a, b: -score(a, b)))
res = 1
for i in range(len(all_packets)):
    if all_packets[i] == [[2]]:
        res *= i + 1
    elif all_packets[i] == [[6]]:
        res *= i + 1
print("Part one:", result)
print("Part two:", res)