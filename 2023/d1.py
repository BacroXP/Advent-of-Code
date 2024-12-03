
lines = open("input.txt").read().strip().split("\n")
replaces = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e",
            "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e", "zero": "z0o"}


def getSolution(lines):
    nums = []

    for line in lines:
        line = line.strip()
        first_digit = None
        last_digit = None

        for char in line:
            if char.isdigit():
                if first_digit is None:
                    first_digit = char
                last_digit = char

        if first_digit is not None and last_digit is not None:
            nums.append(int(first_digit + last_digit))

    print(sum(nums))

getSolution(lines)

replaced_lines = []
for line in lines:
    for replace in replaces:
        line = line.replace(replace, replaces[replace])
    replaced_lines.append(line)

getSolution(replaced_lines)
