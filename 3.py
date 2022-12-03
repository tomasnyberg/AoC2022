import sys
lines = list(map(str.strip, sys.stdin.readlines()))

rucksacks = []
for line in lines:
    rucksacks.append(line)
result = 0
for r in rucksacks:
    a = r[:len(r)//2]
    b = r[len(r)//2:]
    aset = set(a)
    bset = set(b)
    ch = (aset & bset).pop()
    orded = ord(ch)
    if 65 <= orded <= 90:
        result += orded - 65 + 27
    else:
        result += orded - 97 + 1
print(result)