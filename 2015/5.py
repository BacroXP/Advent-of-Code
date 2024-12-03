
test_link = "test.txt"
real_link = "input.txt"


def sol(address):
    words = open(address).read().strip().split("\n")
    sol1 = 0
    sol2 = 0
    
    for word in words:
        if (
            sum(1 for c in word if c in "aeiou") >= 3 and
            any(word[i] == word[i + 1] for i in range(len(word) - 1)) and
            all(sub not in word for sub in ["ab", "cd", "pq", "xy"])
        ):
            sol1 += 1

        if (
            any(word[i:i+2] in word[i+2:] for i in range(len(word) - 1)) and
            any(word[i] == word[i + 2] for i in range(len(word) - 2))
        ):
            sol2 += 1

    print("Solution 1:", sol1)
    print("Solution 2:", sol2)


sol(test_link)
sol(real_link)
