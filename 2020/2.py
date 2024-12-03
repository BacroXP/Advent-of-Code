
data = open("input.txt").read().strip().split("\n")
sol1 = 0
sol2 = 0

for line in data:
    count = 0
    control, password = line.split(":")
    times, letter = control.split(" ")
    password = password[1:]
    minimum, maximum = times.split("-")

    for char in password:
        if char == letter:
            count += 1

    if int(minimum) <= count <= int(maximum):
        sol1 += 1

for line in data:
    control, password = line.split(":")
    times, letter = control.split(" ")
    password = password[1:]
    minimum, maximum = times.split("-")

    if password[int(minimum) - 1: int(minimum)] == letter and password[int(maximum) - 1: int(maximum)] == letter:
        continue
    elif password[int(minimum) - 1: int(minimum)] == letter or password[int(maximum) - 1: int(maximum)] == letter:
        sol2 += 1

print(sol1)
print(sol2)
