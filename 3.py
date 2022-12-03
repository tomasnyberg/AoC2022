import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def getVal(x):
    return ord(x) - ord('a') + 1 if x.islower() else ord(x) - ord('A') + 27

def part_one():
    result = 0
    for line in lines:
        result += getVal((set(line[:len(line)//2]) & set(line[len(line)//2:])).pop())
    return result

def part_two():
    result = 0
    for i in range(0,len(lines), 3):
        ch = (set(lines[i]) & set(lines[i+1]) & set(lines[i+2])).pop()
        result += getVal(ch)
    return result
print("Part one:", part_one())
print("Part two:", part_two())
