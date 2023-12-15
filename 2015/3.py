import sys

directions = {"<": (-1, 0), ">": (1, 0), "^": (0, 1), "v": (0, -1)}

for part1 in [True, False]:
    santa = True
    result = 1
    
    position_santa = {"x": 0, "y": 0}
    position_robo = {"x": 0, "y": 0}
    positions = [[0, 0]]

    with open(sys.argv[1], "r") as file:
        for line in file:
            for char in line:
                if santa or part1:
                    position_santa["x"] += directions[char][0]
                    position_santa["y"] += directions[char][1]
                    if [position_santa["x"], position_santa["y"]] not in positions:
                        result += 1
                        positions.append([position_santa["x"], position_santa["y"]])
                    santa = not santa
                else:
                    position_robo["x"] += directions[char][0]
                    position_robo["y"] += directions[char][1]
                    if [position_robo["x"], position_robo["y"]] not in positions:
                        result += 1
                        positions.append([position_robo["x"], position_robo["y"]])
                    santa = not santa

    print(result)
