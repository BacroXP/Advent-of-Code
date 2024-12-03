import sys

lines = open(sys.argv[-1]).read().strip().split("\n")
sol = 0

for line in lines:
    line = line.split("\t")
    minimum = 10000000000000000
    maximum = 0

    for char in line:
        char = int(char)

        if char < minimum:
            minimum = char
        if char > maximum:
            maximum = char
        
        print(maximum, minimum)
    
    print(maximum, minimum)
    sol += maximum - minimum

print(sol)
