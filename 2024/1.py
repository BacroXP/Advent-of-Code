from collections import Counter


def sol(address):
    input_data = open(address).read().strip()
    cmds = input_data.split('\n')
    left_values = []
    right_values = []
    right_count = Counter()
    
    for cmd in cmds:
        parts = cmd.split()
        if len(parts) == 2:
            left, right = int(parts[0]), int(parts[1])
            left_values.append(left)
            right_values.append(right)
            right_count[right] += 1
    
    p1 = 0
    left_values = sorted(left_values)
    right_values = sorted(right_values)
    
    for l, r in zip(left_values, right_values):
        p1 += abs(r - l)
    
    print("Solution 1: " + str(p1))
    
    p2 = 0
    for l in left_values:
        p2 += l * right_count.get(l, 0)
    
    print("Solution 2: " + str(p2))


test_link = "test.txt"
real_link = "input.txt"

sol(test_link)
sol(real_link)
