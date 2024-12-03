from math import gcd

input_filename = "input.txt"
input_data = open(input_filename).read().strip()
input_lines = input_data.split('\n')


def calculate_lcm(numbers):
    result = 1
    for number in numbers:
        result = (number * result) // gcd(number, result)
    return result


rules_dict = {'L': {}, 'R': {}}
steps, rules_data = input_data.split('\n\n')

for line in rules_data.split('\n'):
    state, transitions = line.split('=')
    state = state.strip()
    left, right = transitions.split(',')
    left = left.strip()[1:].strip()
    right = right[:-1].strip()
    rules_dict['L'][state] = left
    rules_dict['R'][state] = right


def solve(part2):
    current_positions = []
    for state in rules_dict['L']:
        if state.endswith('A' if part2 else 'AAA'):
            current_positions.append(state)

    time_for_positions = {}
    current_time = 0

    while True:
        new_positions = []

        for i, position in enumerate(current_positions):
            position = rules_dict[steps[current_time % len(steps)]][position]

            if position.endswith('Z'):
                time_for_positions[i] = current_time + 1

                if len(time_for_positions) == len(current_positions):
                    return calculate_lcm(time_for_positions.values())

            new_positions.append(position)

        current_positions = new_positions
        current_time += 1


print(solve(False))
print(solve(True))
