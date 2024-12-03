
test_link = "test.txt"
real_link = "input.txt"


def sol(address):
    cmd = open(address).read().strip()
    distr = {"(": 1, ")": -1}
    sol1 = 0
    sol2 = -1
    
    for i, char in enumerate(cmd):
        sol1 += distr[char]
        
        if sol1 == -1 and sol2 == -1:
            sol2 = i + 1
    
    print("Solution 1:" + str(sol1))
    print("Solution 2:" + str(sol2))


sol(test_link)
sol(real_link)
