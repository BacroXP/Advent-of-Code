newData = []


with open('input.txt', 'r') as file:
    for line in file:
        line = line + " "
        first_digit = None
        last_digit = None

        for char in line:
            if char.isdigit():
                if first_digit is None:
                    first_digit = char
                last_digit = char

        if first_digit is not None and last_digit is not None:
            newData.append(int(first_digit + last_digit))


print(sum(newData))
