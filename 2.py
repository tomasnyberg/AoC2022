import sys
lines = list(map(str.strip, sys.stdin.readlines()))


rockscore = 1
paperscore = 2
scissorscore = 3

scores = {'X': 1, 'Y': 2, 'Z': 3}
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
