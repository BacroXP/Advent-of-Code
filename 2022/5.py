
model = [["C", "Z", "N", "B", "M", "W", "Q", "V"],
         ["H", "Z", "R", "W", "C", "B"],
         ["F", "Q", "R", "J"],
         ["Z", "S", "W", "H", "F", "N", "M", "T"],
         ["G", "F", "W", "L", "N", "Q", "P"],
         ["L", "P", "W"],
         ["V", "B", "D", "R", "G", "C", "Q", "J"],
         ["Z", "Q", "N", "B", "W"],
         ["H", "L", "F", "C", "G", "T", "J"]]

moves = open("input.txt").read().strip().split("\n")

for move in moves:
    num_move = move.split(" ")
    num_move.remove("move")
    num_move.remove("from")
    num_move.remove("to")

    from_index = int(num_move[1]) - 1
    to_index = int(num_move[2]) - 1

    for i in range(int(num_move[0])):
        if from_index < len(model) and to_index < len(model) and model[from_index]:
            model[to_index].append(model[from_index].pop())
        else:
            print(f"Invalid move: {move}. Check indices and non-empty source list.")

lasts = ""

for tower in model:
    lasts += tower[len(tower) - 1]

print(lasts)

model = [["C", "Z", "N", "B", "M", "W", "Q", "V"],
         ["H", "Z", "R", "W", "C", "B"],
         ["F", "Q", "R", "J"],
         ["Z", "S", "W", "H", "F", "N", "M", "T"],
         ["G", "F", "W", "L", "N", "Q", "P"],
         ["L", "P", "W"],
         ["V", "B", "D", "R", "G", "C", "Q", "J"],
         ["Z", "Q", "N", "B", "W"],
         ["H", "L", "F", "C", "G", "T", "J"]]

for move in moves:
    num_move = move.split(" ")
    num_move.remove("move")
    num_move.remove("from")
    num_move.remove("to")

    from_index = int(num_move[1]) - 1
    to_index = int(num_move[2]) - 1

    for i in range(int(num_move[0])):
        if from_index < len(model) and to_index < len(model) and model[from_index]:
            model[to_index].append(model[from_index].pop(-1 * (int(num_move[0]) - i)))
        else:
            print(f"Invalid move: {move}. Check indices and non-empty source list.")

lasts = ""

for tower in model:
    lasts += tower[len(tower) - 1]

print(lasts)
