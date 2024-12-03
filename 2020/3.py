
map = open("input.txt").read().strip().split("\n")
xPos, yPos = 0, 0
moveX, moveY = 3, 1
sol1 = 0
sol2 = 1

for i in range(len(map) // moveY - 1):
    xPos += moveX
    yPos += moveY

    if map[yPos][xPos % len(map[yPos])] == "#":
        sol1 += 1

for i, spdX in enumerate([1, 3, 5, 7, 1]):
    xPos, yPos = 0, 0

    if i == 4:
        moveX, moveY = spdX, 2
    else:
        moveX, moveY = spdX, 1

    count = 0

    for i in range(len(map) // moveY - 1):
        xPos += moveX
        yPos += moveY

        if map[yPos][xPos % len(map[yPos])] == "#":
            count += 1

    sol2 *= count

print(sol1)
print(sol2)
