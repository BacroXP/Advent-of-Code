
data = [[]]
total_distance = 0
best_distance = 0

solution = 1

with open("input.txt", "r") as file:
    for y, line in enumerate(file):
        data.append([])
        anz = -1
        row = 0

        for x, char in enumerate(line):
            if char.isdigit():
                if anz == -1:
                    anz = int(char)
                else:
                    anz = int(str(anz) + char)
            elif char == " " and anz != -1:
                data[y].append(anz)
                anz = -1
        if anz != -1:
            data[y].append(anz)
            anz = -1

for i in range(len(data[0])):
    sol = 0

    for j in range(data[0][i]):
        total_distance = j * (data[0][i] - j)

        if total_distance > data[1][i]:
            sol += 1

    solution *= sol

print("Part 1: " + str(solution))
