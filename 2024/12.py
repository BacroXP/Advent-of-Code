import libs.input
from collections import deque

grid = libs.input.file()
rows, cols = len(grid), len(grid[0])
directions = [(-1,0),(0,1),(1,0),(0,-1)]
visited = set()
total_area_perimeter = 0
total_area_sides = 0

for index in range(rows * cols):
    start_row, start_col = divmod(index, cols)

    if (start_row, start_col) in visited:
        continue

    queue = deque([(start_row, start_col)])
    area = 0
    perimeter = 0
    boundary_cells = {}

    while queue:
        r, c = queue.popleft()

        if (r, c) in visited:
            continue

        visited.add((r, c))
        area += 1

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c]:
                queue.append((nr, nc))
            else:
                perimeter += 1
                boundary_cells.setdefault((dr, dc), set()).add((r, c))

    sides = 0

    for side_cells in boundary_cells.values():
        side_seen = set()

        for cell in side_cells:
            if cell in side_seen:
                continue

            sides += 1
            side_queue = deque([cell])

            while side_queue:
                sr, sc = side_queue.popleft()

                if (sr, sc) in side_seen:
                    continue

                side_seen.add((sr, sc))

                for dr, dc in directions:
                    neighbor = (sr + dr, sc + dc)

                    if neighbor in side_cells:
                        side_queue.append(neighbor)

    total_area_perimeter += area * perimeter
    total_area_sides += area * sides

print(total_area_perimeter)
print(total_area_sides)
