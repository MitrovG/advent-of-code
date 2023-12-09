import os
from typing import List

from util.input import read_matrix_num

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix_num(filepath)


def extrapolate_value(sequence: List[int]):

    f_values = []
    b_values = []
    while True:
        f_values.append(sequence[-1])
        b_values.append(sequence[0])
        new_sequence = [b - a for a, b in zip(sequence[:-1], sequence[1:])]
        if any(x != 0 for x in new_sequence):
            sequence = new_sequence
        else:
            f_val = sum(f_values)
            b_val = sum(value if idx % 2 == 0 else -value for idx, value in enumerate(b_values))
            return f_val, b_val


solution_1 = 0
solution_2 = 0
for row in data:
    f_value, b_value = extrapolate_value(row)
    solution_1 += f_value
    solution_2 += b_value

print(solution_1)
print(solution_2)