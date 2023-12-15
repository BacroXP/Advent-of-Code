winning_numbers = []
numbers = []
cards_win = []
value = 0
cards = []

anz_cards = 0

completed_wn = False
began_wn = False

with open("input.txt", "r") as file:
    for y, line in enumerate(file):
        cards.append(1)
        winning_numbers = []
        numbers = []

        completed_wn = False
        anz = 0

        for x, char in enumerate(line):
            if char.isdigit():
                anz = int(str(anz) + char)
            elif char == " ":
                if completed_wn:
                    if anz is not None and anz != 0:
                        numbers.append(anz)
                elif began_wn:
                    if anz is not None and anz != 0:
                        winning_numbers.append(anz)
                anz = 0
            elif char == "|":
                anz = 0
                completed_wn = True
            elif char == ":":
                anz = 0
                began_wn = True

        if anz is not None and anz != 0:
            numbers.append(anz)

        counter = 0

        for i in range(len(winning_numbers)):
            for j in range(len(numbers)):
                if winning_numbers[i] == numbers[j]:
                    counter += 1

        if counter != 0:
            value += 2 ** (counter - 1)

        cards_win.append(counter)

print(cards)

while sum(cards) != 0:
    for i in range(len(cards)):
        if cards_win[i] != 0 or cards != 0:
            for j in range(cards_win[i]):
                cards[(i + j + 1) % len(cards)] += cards[i]
            print(cards)

        anz_cards += cards[i]
        cards[i] = 0
        print(anz_cards)

print(cards)

print("\n Part 1: " + str(value))
print("\n Part 2: " + str(anz_cards))
