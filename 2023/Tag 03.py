from collections import defaultdict


def process_grid(file_content):
    lines = file_content.split('\n')
    grid = [[char for char in line] for line in lines]
    num_rows = len(grid)
    num_columns = len(grid[0])

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


def main():
    # Specify the path to your text file
    file_path = 'input.txt'

    try:
        # Read the content of the text file
        with open(file_path, 'r') as file:
            file_content = file.read().strip()

        # Process the content of the file
        total_sum, number_positions = process_grid(file_content)

        print("Part 1:", total_sum)

        product_of_pairs = 0
        for position, numbers in number_positions.items():
            if len(numbers) == 2:
                product_of_pairs += numbers[0] * numbers[1]

        print("Part 2:", product_of_pairs)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
