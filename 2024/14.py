import libs.input
from collections import deque
import math

dirs = [(-1,0),(0,1),(1,0),(0,-1)]

width, height = 101, 103
robots = libs.input.nums(libs.input.file())

for time in range(1, 10**6):
    grid = [['.'] * width for _ in range(height)]

    if time == 100:
        q = [0, 0, 0, 0]
        mid_x, mid_y = width // 2, height // 2

    for i, (x, y, vx, vy) in enumerate(robots):
        x = (x + vx) % width
        y = (y + vy) % height
        robots[i] = (x, y, vx, vy)
        grid[y][x] = '#'

        if time == 100:
            if x < mid_x and y < mid_y: q[0] += 1
            elif x > mid_x and y < mid_y: q[1] += 1
            elif x < mid_x and y > mid_y: q[2] += 1
            elif x > mid_x and y > mid_y: q[3] += 1

    if time == 100:
        print(math.prod(q))

    components = 0
    seen = set()

    for x in range(width):
        for y in range(height):
            if grid[y][x] == '#' and (x, y) not in seen:
                components += 1
                queue = deque([(x, y)])

                while queue:
                    cx, cy = queue.popleft()
                    if (cx, cy) in seen:
                        continue
                    seen.add((cx, cy))

                    for dx, dy in dirs:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == '#':
                            queue.append((nx, ny))

    if components <= 200:
        print(time)
        break
