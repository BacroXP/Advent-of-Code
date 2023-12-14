import sys

calories = []
anz = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        if len(line) == 1:
            calories.append(anz)
            anz = 0
        else:
            anz += int(line[:-1])

calories.sort()

print("Part 1: " + str(calories[-1]))
print("Part 2: " + str(calories[-1] + calories[-2] + calories[-3]))
