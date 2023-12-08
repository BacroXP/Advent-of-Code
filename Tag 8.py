from math import gcd

# Read input from file specified in command-line argument
input_filename = "input.ex"
input_data = open(input_filename).read().strip()
input_lines = input_data.split('\n')


# Helper function to calculate the least common multiple
def calculate_lcm(numbers):
    result = 1
    for number in numbers:
        result = (number * result) // gcd(number, result)
    return result


# Initialize a dictionary to store left ('L') and right ('R') rules
rules_dict = {'L': {}, 'R': {}}

# Split input data into steps and rules
steps, rules_data = input_data.split('\n\n')

# Process rules and populate the rules dictionary
for line in rules_data.split('\n'):
    state, transitions = line.split('=')
    state = state.strip()
    left, right = transitions.split(',')
    left = left.strip()[1:].strip()
    right = right[:-1].strip()
    rules_dict['L'][state] = left
    rules_dict['R'][state] = right


# Main solver function
def solve(part2):
    # Initialize positions based on rules
    current_positions = []
    for state in rules_dict['L']:
        if state.endswith('A' if part2 else 'AAA'):
            current_positions.append(state)

    # Dictionary to store times for each position
    time_for_positions = {}
    current_time = 0

    # Main loop
    while True:
        new_positions = []

        # Update positions based on rules
        for i, position in enumerate(current_positions):
            position = rules_dict[steps[current_time % len(steps)]][position]

            # Check if a final state is reached
            if position.endswith('Z'):
                time_for_positions[i] = current_time + 1

                # If all positions have times, calculate the least common multiple
                if len(time_for_positions) == len(current_positions):
                    return calculate_lcm(time_for_positions.values())

            new_positions.append(position)

        current_positions = new_positions
        current_time += 1


# Print results for both part1 (False) and part2 (True)
print(solve(False))
print(solve(True))
