
games = open("input.txt").read().strip().split("\n")


def get_win_value(parties):
    sol = 0

    for game in parties:
        you, me = game.split(" ")

        # A, X Rock         1
        # B, Y Paper        2
        # C, Z Scissor      3

        if me == "X":
            if you == "C":
                sol += 7
            elif you == "A":
                sol += 4
            else:
                sol += 1
        elif me == "Y":
            if you == "A":
                sol += 8
            elif you == "B":
                sol += 5
            else:
                sol += 2
        else:
            if you == "B":
                sol += 9
            elif you == "C":
                sol += 6
            else:
                sol += 3

    return sol


print(get_win_value(games))

for i, game in enumerate(games):
    you, sit = game.split(" ")
    literally = {"A": "A", "X": "lose", "B": "B", "Y": "draw", "C": "C", "Z": "win"}

    # create new game
    games[i] = literally[you] + " " + literally[sit]

for i, game in enumerate(games):
    me = ""
    you, sit = game.split(" ")

    if sit == "draw":
        if you == "A":
            me = "X"
        elif you == "B":
            me = "Y"
        else:
            me = "Z"
    elif sit == "win":
        if you == "A":
            me = "Y"
        elif you == "B":
            me = "Z"
        else:
            me = "X"
    else:
        if you == "A":
            me = "Z"
        elif you == "B":
            me = "X"
        else:
            me = "Y"

    games[i] = you + " " + me

print(get_win_value(games))
