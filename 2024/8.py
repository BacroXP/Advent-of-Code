import libs.input

lines = libs.input.file()
antennas = {}
positions = []
antinodes = set()
sol1, sol2 = 0, 0

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != ".":
            if char in antennas:
                positions[antennas[char]].append((x, y))
            else:
                antennas[char] = len(positions)
                positions.append([])
                positions[antennas[char]].append((x, y))

for type in positions:
    for fir in type:
        for sec in type:
            if fir == sec:
                pass
            else:
                vec_x, vec_y = (fir[0] - sec[0]), (fir[1] - sec[1])

                x, y = fir[0] + vec_x, fir[1] + vec_y
                if 0 <= x <= len(lines[0]) and 0 <= y <= len(lines) - 1:
                    antinodes.add((x, y))
                    
                x, y = sec[0] + vec_x, sec[1] + vec_y
                if 0 <= x <= len(lines[0]) and 0 <= y <= len(lines) - 1:
                    antinodes.add((x, y))
                    
                x, y = fir[0] - vec_x, fir[1] - vec_y
                if 0 <= x <= len(lines[0]) and 0 <= y <= len(lines) - 1:
                    antinodes.add((x, y))
                    
                x, y = sec[0] - vec_x, sec[1] - vec_y
                if 0 <= x <= len(lines[0]) and 0 <= y <= len(lines) - 1:
                    antinodes.add((x, y))

for antinode in antinodes:
    if lines[antinode[1]][antinode[0]: antinode[0] + 1] == ".":
        sol1 += 1

print(sol1)
print(sol2)
