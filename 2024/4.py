import libs.input

grid = libs.input.grid()
sol1 = 0
sol2 = 0

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] == "X":
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue

                    nx, ny = x + dx, y + dy

                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]):
                        if grid[nx][ny] == "M":
                            nx, ny = nx + dx, ny + dy

                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]):
                                if grid[nx][ny] == "A":
                                    nx, ny = nx + dx, ny + dy

                                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]):
                                        if grid[nx][ny] == "S":
                                            sol1 += 1

        if grid[x][y] == "A":
            n = []

            for dx in [-1, 1]:
                for dy in [-1, 1]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]):
                        n.append(grid[nx][ny])

            if n.count("M") == 2 == n.count("S") and n != ["S", "M", "M", "S"] and n != ["M", "S", "S", "M"]:
                sol2 += 1

print(sol1)
print(sol2)
