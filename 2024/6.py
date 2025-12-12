import libs.input

grid = libs.input.grid()
grid2 = grid[:]
x, y, dir = None, None, None
positions = set()

for i, row in enumerate(grid):
    for j, el in enumerate(row):
        if el in "<>^v":
            x, y = j, i
            dir = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}[el]
            grid[i][j] = "X"

startx, starty, startdir = x, y, dir
nx, ny = x + dir[0], y + dir[1]

while 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
    if grid[ny][nx] == "#":
        match dir:
            case (1, 0):
                dir = (0, 1)
            case (-1, 0):
                dir = (0, -1)
            case (0, 1):
                dir = (-1, 0)
            case (0, -1):
                dir = (1, 0)
    else:
        grid[y][x] = "X"
        x, y = nx, ny
        positions.add((x, y))
    
    nx, ny = x + dir[0], y + dir[1]

def loop(grid):
    x, y = startx, starty
    dir = startdir
    visited = set()
    
    nx, ny = x + dir[0], y + dir[1]
    
    while 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
        state = (x, y, dir)
        if state in visited:
            return True
        visited.add(state)
        
        if grid[ny][nx] == "#":
            match dir:
                case (1, 0):
                    dir = (0, 1)
                case (-1, 0):
                    dir = (0, -1)
                case (0, 1):
                    dir = (-1, 0)
                case (0, -1):
                    dir = (1, 0)
        else:
            x, y = nx, ny
        
        nx, ny = x + dir[0], y + dir[1]
    
    return False

print(sum([row.count("X") for row in grid]) + 1)
sol2 = 0

for position in positions:
    grid2[position[1]][position[0]] = "#"
    if loop(grid2):
        sol2 += 1
    grid2[position[1]][position[0]] = "."

print(sol2)
