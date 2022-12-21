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

while True:
    progress = False
    to_del = []
    for name, val in unknown.items():
        a, operation, b = val.split()
        if a in known and b in known:
            a = str(known[a])
            b = str(known[b])
            known[name] = eval(a + operation + b)
            to_del.append(name)
            print("evaluating", name, val, known[name])
            progress = True
        else:
            continue
    if not to_del:
        break
    for name in to_del:
        del unknown[name]
print(known)
print(unknown)
print(known['root'])


