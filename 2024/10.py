import libs.input
from collections import deque

grid = libs.input.file()
grid = [[int(x) for x in row] for row in grid]
rows, cols = len(grid), len(grid[0])
dp_cache = {}
sol1, sol2 = 0, 0


def count_paths_bfs(sr, sc):
    queue = deque([(sr, sc)])
    seen = set()
    total = 0

    while queue:
        r, c = queue.popleft()

        if (r, c) in seen:
            continue

        seen.add((r, c))

        if grid[r][c] == 0:
            total += 1

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c] - 1:
                queue.append((nr, nc))

    return total


def count_paths_dfs(r, c):
    if grid[r][c] == 0:
        return 1

    if (r, c) in dp_cache:
        return dp_cache[(r, c)]

    total = 0
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c] - 1:
            total += count_paths_dfs(nr, nc)

    dp_cache[(r, c)] = total

    return total


for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 9:
            sol1 += count_paths_bfs(r, c)
            sol2 += count_paths_dfs(r, c)

print(sol1)
print(sol2)
