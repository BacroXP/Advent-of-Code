with open('input.txt') as file:
    # Read the input file, strip extra whitespaces, and split by lines
    input_data = file.read().strip().split('\n')

# Convert the input data into a list of lists of integers
input_list = [list(map(int, line.split())) for line in input_data]


class NumberSequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.sequence_map = self.map_sequence()
        self.next_number = self.generate_next_number()
        self.previous_number = self.generate_previous_number()

    def __repr__(self):
        return f'{self.sequence_map}'

    def map_sequence(self):
        mapped_sequence = [self.sequence]
        current_sequence = self.sequence

        # Continue mapping until all elements become zero
        while any(num != 0 for num in current_sequence):
            current_sequence = [current_sequence[i + 1] - current_sequence[i] for i in range(len(current_sequence) - 1)]
            mapped_sequence.append(current_sequence)

        return mapped_sequence

    def generate_next_number(self):
        next_num = 0

        # Sum the last elements of each mapped sequence
        for seq in self.sequence_map[::-1]:
            next_num += seq[-1]

        return next_num

    def generate_previous_number(self):
        prev_num = 0

        # Reverse the mapped sequence and calculate the previous number
        for seq in self.sequence_map[::-1]:
            prev_num = seq[0] - prev_num

        return prev_num


# Create NumberSequence instances for each input sequence
number_sequences = [NumberSequence(seq) for seq in input_list]

# Print the results
print('Part 1:', sum(sequence.next_number for sequence in number_sequences))
print('Part 2:', sum(sequence.previous_number for sequence in number_sequences))
