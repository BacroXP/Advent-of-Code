
numbers = open("input.txt").read().strip().split("\n")
sol = ""
erg = 5

for number in numbers:
    for cmd in number:
        if cmd == "L" and erg not in [1, 4, 7]:
            erg -= 1
        elif cmd == "R" and erg not in [3, 6, 9]:
            erg += 1
        elif cmd == "U" and erg not in [1, 2, 3]:
            erg -= 3
        elif cmd == "D" and erg not in [7, 8, 9]:
            erg += 3

    sol += str(erg)

print(sol)

sol = ""
erg = 5

for number in numbers:
        for cmd in number:
            if cmd == "L" and erg not in [1, 2, 5, 10, 13]:
                erg -= 1
            elif cmd == "R" and erg not in [1, 4, 9, 12, 13]:
                erg += 1
            elif cmd == "U" and erg not in [1, 2, 4, 5, 9]:
                if erg in [3, 13]:
                    erg -= 2
                else:
                    erg -= 4
            elif cmd == "D" and erg not in [5, 9, 10, 12, 13]:
                if erg in [1, 11]:
                    erg += 2
                else:
                    erg += 4

        sol += hex(erg)[2:]

print(sol)
