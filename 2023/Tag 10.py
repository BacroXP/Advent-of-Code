from collections import deque

filepath = "input.txt"

file = open(filepath).read().strip()
line = file.split('\n')

grid = [[c for c in row] for row in line]
row = len(grid)
column = len(grid[0])

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]
dist = 0

sr, sc, sd = None, None, None

for r in range(row):
    for c in range(column):
        if grid[r][c] == 'S':
            sr, sc = r, c
            up_valid = (grid[r-1][c] in ['|', '7', 'F'])
            right_valid = (grid[r][c+1] in ['-', '7', 'J'])
            down_valid = (grid[r+1][c] in ['|', 'L', 'J'])
            left_valid = (grid[r][c-1] in ['-', 'L', 'F'])
            assert sum([up_valid, right_valid, down_valid, left_valid]) == 2
            if up_valid and down_valid:
                grid[r][c] = '|'
                sd = 0
            elif up_valid and right_valid:
                grid[r][c] = 'L'
                sd = 0
            elif up_valid and left_valid:
                grid[r][c] = 'J'
                sd = 0
            elif down_valid and right_valid:
                grid[r][c] = 'F'
                sd = 2
            elif down_valid and left_valid:
                grid[r][c] = '7'
                sd = 2
            elif left_valid and right_valid:
                grid[r][c] = '-'
                sd = 1
            else:
                assert False

r = sr
c = sc
d = sd

while True:
    dist += 1
    r += DR[d]
    c += DC[d]
    if grid[r][c] == 'L':
        if d not in [2, 3]:
            break
        elif d == 2:
            d = 1
        else:
            d = 0
    if grid[r][c] == 'J':
        if d not in [1, 2]:
            break
        elif d == 1:
            d = 0
        else:
            d = 3
    if grid[r][c] == '7':
        if d not in [0, 1]:
            break
        elif d == 0:
            d = 3
        else:
            d = 2
    if grid[r][c] == 'F':
        if d not in [0, 3]:
            break
        elif d == 0:
            d = 1
        else:
            d = 2
    assert grid[r][c] != '.'
    if (r, c) == (sr, sc):
        print(dist//2)
        break

R2 = 3 * row
C2 = 3 * column
G2 = [['.' for _ in range(C2)] for _ in range(R2)]

for r in range(row):
    for c in range(column):
        if grid[r][c] == '|':
            G2[3*r+0][3*c+1] = 'x'
            G2[3*r+1][3*c+1] = 'x'
            G2[3*r+2][3*c+1] = 'x'
        elif grid[r][c] == '-':
            G2[3*r+1][3*c+0] = 'x'
            G2[3*r+1][3*c+1] = 'x'
            G2[3*r+1][3*c+2] = 'x'
        elif grid[r][c] == '7':
            G2[3*r+1][3*c+0] = 'x'
            G2[3*r+1][3*c+1] = 'x'
            G2[3*r+2][3*c+1] = 'x'
        elif grid[r][c] == 'F':
            G2[3*r+2][3*c+1] = 'x'
            G2[3*r+1][3*c+1] = 'x'
            G2[3*r+1][3*c+2] = 'x'
        elif grid[r][c] == 'J':
            G2[3*r+1][3*c+0] = 'x'
            G2[3*r+1][3*c+1] = 'x'
            G2[3*r+0][3*c+1] = 'x'
        elif grid[r][c] == 'L':
            G2[3*r+0][3*c+1] = 'x'
            G2[3*r+1][3*c+1] = 'x'
            G2[3*r+1][3*c+2] = 'x'
        elif grid[r][c] == '.':
            pass
        else:
            assert False, grid[r][c]

Q = deque()
SEEN = set()

for r in range(R2):
    Q.append((r, 0))
    Q.append((r, C2-1))

for c in range(C2):
    Q.append((0, c))
    Q.append((R2-1, c))

while Q:
    r, c = Q.popleft()

    if (r, c) in SEEN:
        continue

    if not (0 <= r < R2 and 0 <= c < C2):
        continue

    SEEN.add((r, c))

    if G2[r][c] == 'x':
        continue

    for d in range(4):
        Q.append((r+DR[d], c+DC[d]))

ans = 0

for r in range(row):
    for c in range(column):
        seen = False
        for rr in [0, 1, 2]:
            for cc in [0, 1, 2]:
                if (3*r+rr, 3*c+cc) in SEEN:
                    seen = True
        if not seen:
            ans += 1

print(ans)
