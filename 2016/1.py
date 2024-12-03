
def calculate_distance(moves):
    direction = 0
    x, y = 0, 0

    for move in moves:
        rotation = move[0]
        steps = int(move[1:])

        if rotation == "R":
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

        if direction == 0:
            y += steps
        elif direction == 1:
            x += steps
        elif direction == 2:
            y -= steps
        elif direction == 3:
            x -= steps

    return abs(x) + abs(y)


def find_first_revisited_position(moves):
    direction = 0
    x, y = 0, 0
    visited = set()
    visited.add((0,0))

    for move in moves:
        rotation = move[0]
        steps = int(move[1:])

        if rotation == "R":
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

        for _ in range(steps):
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1

            if (x, y) in visited:
                return abs(x) + abs(y)
            else:
                visited.add((x, y))

    return None


input_file = "input.txt"
moves = open(input_file,).read().strip().split(", ")

distance = calculate_distance(moves)
print("Distance to HQ:", distance)

revisited_distance = find_first_revisited_position(moves)
if revisited_distance:
    print("Distance to first revisited position:", revisited_distance)
else:
    print("No revisited position found.")
