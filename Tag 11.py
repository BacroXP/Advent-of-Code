
def read_input(file_path):
    with open(file_path) as file:
        data = file.read().strip()
    return data.split('\n')


def find_empty_rows(matrix):
    size = len(matrix)
    empty_row_indices = []

    for i in range(size):
        is_empty = all(cell == '.' for cell in matrix[i])
        if is_empty:
            empty_row_indices.append(i)

    return empty_row_indices


def find_empty_cols(matrix):
    size = len(matrix[0])
    empty_col_indices = []

    for i in range(size):
        is_empty = all(row[i] == '.' for row in matrix)
        if is_empty:
            empty_col_indices.append(i)

    return empty_col_indices


def main(file_path):
    raw_data = read_input(file_path)
    galaxy_map = [list(row) for row in raw_data]
    rows, cols = len(galaxy_map), len(galaxy_map[0])

    for row in galaxy_map:
        assert len(row) == cols

    empty_rows = find_empty_rows(galaxy_map)
    empty_cols = find_empty_cols(galaxy_map)

    galaxies = [(r, c) for r in range(rows) for c in range(cols) if galaxy_map[r][c] == '#']

    for part2 in [False, True]:
        expansion_factor = 10**6 - 1 if part2 else 2 - 1
        total_distance = 0

        for i, (r, c) in enumerate(galaxies):
            for j in range(i, len(galaxies)):
                r2, c2 = galaxies[j]
                distance = abs(r2 - r) + abs(c2 - c)

                for er in empty_rows:
                    if min(r, r2) <= er <= max(r, r2):
                        distance += expansion_factor

                for ec in empty_cols:
                    if min(c, c2) <= ec <= max(c, c2):
                        distance += expansion_factor

                total_distance += distance

        print(total_distance)


if __name__ == "__main__":
    file_path = "input.txt"  # Replace this with the actual file path
    main(file_path)
