import sys
lines = list(map(str.strip, sys.stdin.readlines()))

known = {}
unknown = {}
for line in lines:
    name, op = line.split(": ")
    # if op is a digit
    if op[0].isdigit():
        known[name] = int(op)
    else:
        unknown[name] = op

def attempt_eval(num, known, unknown):
    known['humn'] = num
    while True:
        progress = False
        to_del = []
        for name, val in unknown.items():
            a, operation, b = val.split()
            if a in known and b in known:
                if name == 'root':
                    print("EVALUATING ROOT", num, known[a], known[b])
                    return known[a] > known[b]
                    # if known[a] > known[b]:
                    #     return -1
                    # if known[a] == known[b]:
                    #     return 0
                    # if known[a] < known[b]:
                    #     return 1
                    # return known[a] == known[b]
                a = str(known[a])
                b = str(known[b])
                known[name] = eval(a + operation + b)
                to_del.append(name)
                # print("evaluating", name, val, known[name])
                progress = True
            else:
                continue
        if not to_del:
            break
        for name in to_del:
            del unknown[name]
    

print(attempt_eval(0, known.copy(), unknown.copy()))


print(attempt_eval(3272260914328, known.copy(), unknown.copy()))


# Making human bigger makes a smaller
def bs():
    low = 0
    high = 10000000000000
    while low < high:
        mid = (low + high) // 2
        res = attempt_eval(mid, known.copy(), unknown.copy())
        if res:
            low = mid + 1
        else:
            high = mid
    return low + 1

# print(bs())

# for i in range(10000):
#     # copy known and unknown
#     known_copy = known.copy()
#     unknown_copy = unknown.copy()
#     if attempt_eval(i, known_copy, unknown_copy):
#         print("FOUND", i)
#         break
# print(known)
# print(unknown)
# print(known['root'])


