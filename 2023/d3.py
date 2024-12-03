from collections import defaultdict


def process_grid():
    grid = [[char for char in line] for line in lines]
    num_rows = len(lines)
    num_columns = len(lines[0])
    total_sum = 0
    number_positions = defaultdict(list)

    for row in range(num_rows):
        adjacent_gears = set()
        current_number = 0
        has_part = False

        for col in range(len(grid[row]) + 1):
            if col < num_columns and grid[row][col].isdigit():
                current_number = current_number * 10 + int(grid[row][col])

                for row_offset in [-1, 0, 1]:
                    for col_offset in [-1, 0, 1]:
                        new_row = row + row_offset
                        new_col = col + col_offset

                        if 0 <= new_row < num_rows and 0 <= new_col < num_columns:
                            neighbor_char = grid[new_row][new_col]

                            if not neighbor_char.isdigit() and neighbor_char != '.':
                                has_part = True
                            if neighbor_char == '*':
                                adjacent_gears.add((new_row, new_col))

            elif current_number > 0:
                for gear_position in adjacent_gears:
                    number_positions[gear_position].append(current_number)
                if has_part:
                    total_sum += current_number
                current_number = 0
                has_part = False
                adjacent_gears = set()

    return total_sum, number_positions


lines = open("input.txt").read().strip().split('\n')

total_sum, number_positions = process_grid()
product_of_pairs = sum([numbers[0] * numbers[1] if len(numbers) == 2 else 0 for _, numbers in number_positions.items()])

print(total_sum)
print(product_of_pairs)
