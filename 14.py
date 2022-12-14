import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

# 1000 * 1000 matrix
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
                # print(y, x)
print(max_y)

for i in range(len(matrix[max_y+2])):
    matrix[max_y+2][i] = 1
def print_matrix():
    for r in range(15):
        for c in matrix[r][490:505]:
            if c == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()
    # print(*matrix[r][490:505])
# print(all_lines)
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
        print("sand landed at", r, c)
        # print_matrix()
        break
    if r > 980:
        return True
        

for i in range(100000):
    if sand():
        print(i)
        break

            

