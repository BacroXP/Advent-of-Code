rocks = []


def rotate(stones):
    len_r = len(stones)
    len_c = len(stones[0])
    new_stones = [['?' for _ in range(len_r)] for _ in range(len_c)]
    for r in range(len_r):
        for c in range(len_c):
            new_stones[c][len_r - 1 - r] = stones[r][c]
    return new_stones


def roll_stones(stones):
    anz = 1

    while anz != 0:
        anz = 0
        for y in range(len(stones)):
            for x in range(len(stones[y])):
                if y != 0:
                    if stones[y][x] == "O" and stones[y - 1][x] == ".":
                        stones[y - 1][x] = "O"
                        stones[y][x] = "."

                        anz += 1

    return stones


def find_weight(stones):
    force = 0

    for i in range(len(stones)):
        for j in range(len(stones[i])):
            if stones[i][j] == "O":
                force += len(stones) - i

    print(force)


with open("input.txt", "r") as file:
    for y, line in enumerate(file):
        rocks.append([])
        for char in line:
            if char != "\n":
                rocks[y].append(char)

rock_formations = {}
target = 10 ** 9
t = 0

while t < target:
    for dir in range(4):
        rocks = roll_stones(rocks)
        if t == 0 and dir == 0:
            find_weight(rocks)
        rocks = rotate(rocks)
        rock_formation = tuple(tuple(row) for row in rocks)
        if rock_formation in rock_formations:
            cycle_length = t - rock_formations[rock_formation]
            amt = (target - t) // cycle_length
            t += amt * cycle_length
        rock_formations[rock_formation] = t
    t += 1

find_weight(rocks)
