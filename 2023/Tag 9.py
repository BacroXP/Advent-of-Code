with open('input.txt') as file:
    input_data = file.read().strip().split('\n')

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

        while any(num != 0 for num in current_sequence):
            current_sequence = [current_sequence[i + 1] - current_sequence[i] for i in range(len(current_sequence) - 1)]
            mapped_sequence.append(current_sequence)

        return mapped_sequence

    def generate_next_number(self):
        next_num = 0

        for seq in self.sequence_map[::-1]:
            next_num += seq[-1]

        return next_num

    def generate_previous_number(self):
        prev_num = 0

        for seq in self.sequence_map[::-1]:
            prev_num = seq[0] - prev_num

        return prev_num


number_sequences = [NumberSequence(seq) for seq in input_list]

print('Part 1:', sum(sequence.next_number for sequence in number_sequences))
print('Part 2:', sum(sequence.previous_number for sequence in number_sequences))
