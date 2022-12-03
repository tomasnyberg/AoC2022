import sys
lines = list(map(str.strip, sys.stdin.readlines()))

rucksacks = []
for line in lines:
    rucksacks.append(line)
result = 0
taken = set()
for i in range(0,len(rucksacks), 3):
    chars = set(rucksacks[i])
    chars &= set(rucksacks[i+1])
    chars &= set(rucksacks[i+2])
    ch = chars.pop()
    orded = ord(ch)
    if 65 <= orded <= 90:
        result += orded - 65 + 27
    else:
        result += orded - 97 + 1
print(result)
