import sys

ribbon = 0

with open(sys.argv[-1], "r") as file:
    for line in file:
        line += "x"
        packet = []
        anz = -1

        for char in line:
            if char == "x" and anz != -1:
                packet.append(anz)
                anz = -1
            else:
                if anz == -1:
                    anz = int(char)
                else:
                    anz = int(str(anz) + char)

        packet.sort()

        ribbon += 2 * packet[0]
        ribbon += 2 * packet[1]
        ribbon += packet[0] * packet[1] * packet[2]

print(ribbon)
