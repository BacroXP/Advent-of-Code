import libs.input

nums = libs.input.nums(libs.input.file())
sol1, sol2 = 0, 0


def save(arr):
    temp = sorted(arr)

    if (arr == temp or arr == temp[::-1]):
        if all(0 < abs(num1 - num2) < 4 for num1, num2 in libs.input.pairs(arr)):
            return True
    
    return False


for row in nums:
    if save(row):
        sol1 += 1
    
    if not all(not save(row[:i] + row[i + 1:]) for i in range(len(row))):
        print(row)
        sol2 += 1

print(sol1)
print(sol2)
