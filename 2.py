import sys
lines = list(map(str.strip, sys.stdin.readlines()))

scores = {'X': 1, 'Y': 2, 'Z': 3}
beats = {'Y': 'A', 'Z': 'B', 'X': 'C'}
loses = {'A': 'Y', 'B': 'Z', 'C': 'X'}
equals = {'X': 'A', 'Y': 'B', 'Z': 'C'}

def part_one():
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
print(part_one())


result = 0
for line in lines:
    split = line.split(" ")
    # result += scores[split[1]]
    if split[1] == 'Y':
        result += 3
        if split[0] == 'A':
            result += 1
        elif split[0] == 'B':
            result += 2
        else:
            result += 3
    elif split[1] == 'Z':
        result += 6
        if split[0] == 'A':
            result += 2
        elif split[0] == 'B':
            result += 3
        else:
            result += 1
    else:
        if split[0] == 'A':
            result += 3
        elif split[0] == 'B':
            result += 1
        else:
            result += 2
    #     elif split[1] == "Y":
    #         result += 6
    # if split[0] == 'B':
    #     if split[1] == "Z":
    #         result += 6
    #     elif split[1] == "Y":
    #         result += 3
    # if split[0] == 'C':
    #     if split[1] == "X":
    #         result += 6
    #     elif split[1] == "Z":
    #         result += 3
print(result)
