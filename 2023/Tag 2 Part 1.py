colors = ["blue", "green", "red"]
color_anz = [0, 0, 0]
color_line = [0, 0, 0]
anz = "0"
total_legit = 0
legit = True


with open("input.txt", "r") as file:
    for i, line in enumerate(file):
        legit = True
        color_line = [0, 0, 0]

        for char in line:
            if char.isdigit():
                anz += char
            else:
                if char == "b":
                    if int(anz) > 14:
                        legit = False
                    anz = "0"
                elif char == "g":
                    if int(anz) > 13:
                        legit = False
                    anz = "0"
                elif char == "r":
                    if int(anz) > 12:
                        legit = False
                    anz = "0"
                elif char == ":":
                    anz = "0"
        if legit:
            total_legit += i + 1

print(total_legit)
