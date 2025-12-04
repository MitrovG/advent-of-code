import os

from util.input import read_matrix

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix(filepath)

for x in [2, 12]:
    solution = 0
    for bank in data:
        current = [-1] * x
        for idx, battery in enumerate(bank):
            start_position = max(len(current) - len(bank) + idx, 0)
            for current_idx, current_battery in enumerate(current[start_position:]):
                if battery > current_battery:
                    current = current[:current_idx + start_position] + [battery]
                    current = current + [-1] * (x - len(current))
                    break

        joltage = int("".join(map(str, current)))
        solution += joltage

    print(solution)
