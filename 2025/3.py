import libs.input

sol1, sol2 = 0, 0


def get_max(nums, left):
    return max(nums[: len(nums) - left]), nums[nums.index(max(nums[: len(nums) - left])) + 1 :]


for line in libs.input.file():
    nums = list(map(int, line))
    biggest, nums = get_max(nums, 1)
    sol1 += int(str(biggest) + str(get_max(nums, 0)[0]))

    nums = [int(c) for c in line]
    
    for i in range(12):
        biggest, nums = get_max(nums, 11 - i)
        sol2 += biggest * (10 ** (11 - i))

print("Part 1:", sol1)
print("Part 2:", sol2)
