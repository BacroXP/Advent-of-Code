
new_mass = 0
fuel = 0


def get_fuel(m):
    extra_mass = (int(m) // 3) - 2

    if m < 3:
        return extra_mass, 0
    else:
        return extra_mass, get_fuel(extra_mass)[1] + extra_mass


for mass in open("input.txt").read().strip().split("\n"):
    new_mass += get_fuel(int(mass))[0]
    fuel += get_fuel(int(mass))[1]

print(new_mass)
print(fuel)
