
sum = 2020
part1 = True
part2 = True

entries = open("input.txt").read().strip().split("\n")

for i, entry1 in enumerate(entries):
    for j, entry2 in enumerate(entries):
        if i != j:
            if int(entry1) + int(entry2) == sum and part1:
                print(int(entry1) * int(entry2))
                part1 = False

for i, entry1 in enumerate(entries):
    for j, entry2 in enumerate(entries):
        for k, entry3 in enumerate(entries):
            if i != j and i != k and j != k:
                if int(entry1) + int(entry2) + int(entry3) == sum and part2:
                    print(int(entry1) * int(entry2) * int(entry3))
                    part2 = False
