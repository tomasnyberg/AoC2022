import sys
lines = list(map(str.strip, sys.stdin.readlines()))

scores = {'X': 1, 'Y': 2, 'Z': 3}
def part_one():
    equals = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    beats = {'Y': 'A', 'Z': 'B', 'X': 'C'}
    def get_score(a, b):
        if equals[b] == a:
            return 3
        if beats[b] == a:
            return 6
        return 0
    result = 0
    for line in lines:
        a, b = line.split()
        result += get_score(a, b) + scores[b]
    return result

def part_two():
    p2scores = {'X': 0, 'Y': 3, 'Z': 6}
    beatsp2 = {'A':'Y', 'B':'Z', 'C':'X'}
    loses = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    equalsp2 = {'A':'X', 'B':'Y', 'C':'Z'}
    result = 0
    for line in lines:
        a, b = line.split()
        result += p2scores[b]
        if b == 'X':
            result += scores[loses[a]]
        elif b == 'Y':
            result += scores[equalsp2[a]]
        else:
            result += scores[beatsp2[a]]
    return result

print(part_one())
print(part_two())
