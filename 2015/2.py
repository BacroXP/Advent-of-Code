import sys

dimensions = []

with open(sys.argv[-1], "r") as file:
    for line in file:
        anz = -1
        paket = []
        line += "x"

        for char in line:
            if char.isdigit():
                if anz == -1:
                    anz = int(char)
                else:
                    anz = int(str(anz) + char)
            if char == "x" and anz != -1:
                paket.append(anz)
                anz = -1

        paket.sort()
        print(paket)
        dimensions.append(paket)

wrapping_paper = 0
ribbon = 0

for id in range(len(dimensions)):
    wrapping_paper += 2 * dimensions[id][0] * dimensions[id][1]
    wrapping_paper += 2 * dimensions[id][1] * dimensions[id][2]
    wrapping_paper += 2 * dimensions[id][2] * dimensions[id][0]
    wrapping_paper += dimensions[id][0] * dimensions[id][1]

    ribbon += 2 * dimensions[id][0]
    ribbon += 2 * dimensions[id][1]
    ribbon += 2 * dimensions[id][2]
    ribbon += dimensions[id][0] * dimensions[id][1] * dimensions[id][2]

print(wrapping_paper)
print(ribbon)
