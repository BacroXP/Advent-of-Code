import libs.input

inp = libs.input.grid()
sol1 = 0
sol2 = 0
i = 1


def liftable():
    j = 0

    for x in range(len(inp)):
        for y in range(len(inp[0])):
            i = 0

            for dx, dy in [(-1, -1), (-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(inp) and 0 <= ny < len(inp[0]):
                    if inp[nx][ny] == "@" or inp[nx][ny] == "x":
                        i += 1
        
            if i < 4 and inp[x][y] == "@":
                inp[x][y] = "x"
                j += 1
    
    for x in range(len(inp)):
        for y in range(len(inp[0])):
            if inp[x][y] == "x":
                inp[x][y] = "."

    return j


while i > 0:
    i = liftable()

    if not sol1:
        sol1 += i

    sol2 += i

print(sol1)
print(sol2)
