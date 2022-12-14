import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

matrix = [[0 for i in range(1000)] for j in range(1000)]
all_lines = []
for line in lines:
    split = line.split(" -> ")
    currline = []
    for s in split:
        currline.append(list(map(int, re.findall(r'\d+', s))))
    all_lines.append(currline)
max_y = 0
for line in all_lines:
    for i in range(1, len(line)):
        x1, y1 = line[i-1]
        x2, y2 = line[i]
        max_y = max(max_y, y1, y2)
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                matrix[y][x] = 1

for i in range(len(matrix[max_y+2])):
    matrix[max_y+2][i] = 1
def sand():
    r = 0
    c = 500
    if matrix[r][c] == 1:
        return True
    while r < 999:
        # print(r, c)
        if matrix[r+1][c] == 0:
            r+=1
            continue
        if matrix[r+1][c-1] == 0:
            c-=1
            continue
        if matrix[r+1][c+1] == 0:
            c+=1
            continue
        matrix[r][c] = 1
        break
    if r > 980:
        return True

def solve():
    for i in range(100000):
        if sand():
            return i

print("Part two:", solve())
