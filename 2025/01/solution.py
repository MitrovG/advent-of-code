import os

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)

dial = 50
solution_1 = 0
solution_2 = 0
for rotation in data:
    direction_sign = rotation[0]
    rotation_num = int(rotation[1:])
    new_dial = dial + rotation_num if direction_sign == 'R' else dial - rotation_num

    if new_dial > 0:
        solution_2 += new_dial // 100
    else:
        solution_2 += abs((new_dial - 1) // 100)
        if dial == 0:
            solution_2 -= 1
    dial = new_dial % 100
    if not dial:
        solution_1 += 1

print(solution_1)
print(solution_2)
