colors = ["blue", "green", "red"]
color_anz = [0, 0, 0]
color_line = [0, 0, 0]
anz = "0"
total_legit = 0
legit = True


with open("your_file.txt", "r") as file:
    for i, line in enumerate(file):
        legit = True
        color_line = [0, 0, 0]

        for char in line:
            if char.isdigit():
                anz += char
            else:
                if char == "b":
                    if int(anz) > color_line[0]:
                        color_line[0] = int(anz)
                    anz = "0"
                elif char == "g":
                    if int(anz) > color_line[1]:
                        color_line[1] = int(anz)
                    anz = "0"
                elif char == "r":
                    if int(anz) > color_line[2]:
                        color_line[2] = int(anz)
                    anz = "0"
                elif char == ":":
                    anz = "0"
        total_legit += color_line[0] * color_line[1] * color_line[2]

print(total_legit)
