import sys
lines = list(map(str.strip, sys.stdin.readlines()))

scores = {chr(i):i-38 for i in range(65,91)}
for i in range(97, 123):
    scores[chr(i)] = i-96 
def part_one():
    result = 0
    for line in lines:
        result += scores[(set(line[:len(line)//2]) & set(line[len(line)//2:])).pop()]
    return result

def part_two():
    result = 0
    for i in range(0,len(lines), 3):
        ch = (set(lines[i]) & set(lines[i+1]) & set(lines[i+2])).pop()
        result += scores[ch]
    return result
print("Part one:", part_one())
print("Part two:", part_two())
