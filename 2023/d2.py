
games = open("input.txt").read().strip().split("\n")
solution = 0
solution2 = 0

for i, game in enumerate(games):
    red, blue, green = 0, 0, 0
    for round in game.split(": ")[1].split("; "):

        for values in round.split(", "):
            value, id = values.split(" ")

            match id:
                case "red":
                    if red < int(value):
                        red = int(value)
                case "blue":
                    if blue < int(value):
                        blue = int(value)
                case "green":
                    if green < int(value):
                        green = int(value)
    
    if 12 >= red and 13 >= green and 14 >= blue:
        solution += i + 1
    
    solution2 += red * blue * green

print(solution)
print(solution2)
