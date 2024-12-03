
with open("input.txt") as f:
    lines = f.readlines()

valid_triangles = 0

for line in lines:
    sides = list(map(int, line.strip().split()))

    sides.sort()

    if sides[0] + sides[1] > sides[2]:
        valid_triangles += 1

print(valid_triangles)

valid_triangles = 0

for i in range(0, len(lines), 3):
    triangle1 = list(map(int, lines[i].strip().split()))
    triangle2 = list(map(int, lines[i + 1].strip().split()))
    triangle3 = list(map(int, lines[i + 2].strip().split()))

    for sides in zip(triangle1, triangle2, triangle3):
        sides = sorted(sides)

        if sides[0] + sides[1] > sides[2]:
            valid_triangles += 1

print(valid_triangles)
