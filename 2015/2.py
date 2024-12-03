def sol(address):
    details = [line.split("x") for line in open(address).read().strip().split("\n")]
    
    sol1 = 0
    sol2 = 0
    
    for detail in details:
        dimensions = sorted(map(int, detail))

        l, w, h = dimensions
        sol1 += 2 * (l * w + w * h + h * l)
        sol1 += l * w

        sol2 += 2 * (l + w)
        sol2 += l * w * h

    print("Solution 1: " + str(sol1))
    print("Solution 2: " + str(sol2))


test_link = "test.txt"
real_link = "input.txt"

sol(test_link)
sol(real_link)
