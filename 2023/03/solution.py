import os

from util.input import read_matrix_str

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix_str(filepath)
gears = {}


def is_adjacent_symbol(number: int, row_: int, col_: int):
    flag = False
    xx = [row_ - 1, row_, row_ + 1]
    yy = list(range(col_ - len(str(number)) - 1, col_ + 1))
    for x in xx:
        if x < 0 or x >= len(data):
            continue
        for y in yy:
            if y < 0 or y >= len(data[0]):
                continue
            val_ = data[x][y]
            if not (val_.isdigit() or val_ == '.'):
                flag = True
                if val_ == '*':
                    gears.setdefault((x, y), []).append(current_number)

    return flag


solution_1 = 0
solution_2 = 0
current_number = 0
for idx_r, row in enumerate(data):
    for idx_c, value in enumerate(row + ['.']):
        if value.isdigit():
            current_number = current_number * 10 + int(value)
        else:
            if current_number > 0:
                if is_adjacent_symbol(current_number, idx_r, idx_c):
                    solution_1 += current_number
                current_number = 0

print(solution_1)
for key, value in gears.items():
    if len(value) == 2:
        solution_2 += (value[0] * value[1])
print(solution_2)
