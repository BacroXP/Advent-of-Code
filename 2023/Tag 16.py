input_file_path = "input.txt"
lines = open(input_file_path).read().strip().split('\n')

grid = [[character for character in row] for row in lines]

num_rows = len(grid)
num_cols = len(grid[0])

ROW_CHANGE = [-1, 0, 1, 0]
COL_CHANGE = [0, 1, 0, -1]

max_score = 0


def move(x, y, direction):
    return (x + ROW_CHANGE[direction], y + COL_CHANGE[direction], direction)


def calculate_score(start_row, start_col, start_direction):
    positions = [(start_row, start_col, start_direction)]
    visited_positions = set()
    visited_positions_twice = set()

    while True:
        new_positions = []

        if not positions:
            break

        for (row, col, direction) in positions:
            if 0 <= row < num_rows and 0 <= col < num_cols:
                visited_positions.add((row, col))

                if (row, col, direction) in visited_positions_twice:
                    continue

                visited_positions_twice.add((row, col, direction))
                current_char = grid[row][col]

                if current_char == '.':
                    new_positions.append(move(row, col, direction))
                    
                elif current_char == '/':
                    new_positions.append(move(row, col, {0: 1, 1: 0, 2: 3, 3: 2}[direction]))
                    
                elif current_char == '\\':
                    new_positions.append(move(row, col, {0: 3, 1: 2, 2: 1, 3: 0}[direction]))
                    
                elif current_char == '|':
                    if direction in [0, 2]:
                        new_positions.append(move(row, col, direction))
                        
                    else:
                        new_positions.append(move(row, col, 0))
                        new_positions.append(move(row, col, 2))
                        
                elif current_char == '-':
                    if direction in [1, 3]:
                        new_positions.append(move(row, col, direction))
                        
                    else:
                        new_positions.append(move(row, col, 1))
                        new_positions.append(move(row, col, 3))
                        
                else:
                    assert False

        positions = new_positions

    return len(visited_positions)


print(calculate_score(0, 0, 1))

for row in range(num_rows):
    max_score = max(max_score, calculate_score(row, 0, 1))
    max_score = max(max_score, calculate_score(row, num_cols - 1, 3))

for col in range(num_cols):
    max_score = max(max_score, calculate_score(0, col, 2))
    max_score = max(max_score, calculate_score(num_rows - 1, col, 0))

print(max_score)
