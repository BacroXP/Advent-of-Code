import libs.input
from libs.efficiency import memoization
from collections import deque

inp = libs.input.file()

for y, row in enumerate(inp):
    for x, c in enumerate(row):
        if c == "S":
            start_y, start_x = y, x

@memoization
def score(y, x):
    if y + 1 == len(inp):
        return 1
    down = inp[y + 1][x]
    if down == "^":
        return score(y + 1, x - 1) + score(y + 1, x + 1)
    return score(y + 1, x)

sol1 = 0
queue = deque([(start_y, start_x)])
seen = set()

while queue:
    y, x = queue.popleft()
    if (y, x) in seen:
        continue
    seen.add((y, x))

    if y + 1 == len(inp):
        continue

    down = inp[y + 1][x]
    if down == "^":
        queue.append((y + 1, x - 1))
        queue.append((y + 1, x + 1))
        sol1 += 1
    else:
        queue.append((y + 1, x))

print(sol1)
print(score(start_y, start_x))
