import os

from util.input import read_matrix_str

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix_str(filepath)


def is_toilet_paper(x, xx, y, yy):
    return 0 <= x + xx < len(data) and 0 <= y + yy < len(data[0]) and data[x + xx][y + yy] == '@'


solution_1 = 0
solution_2 = 0
flag = True
while True:
    removable = []
    for idx_r, row in enumerate(data):
        for idx_c, value in enumerate(row):
            if value == '@':
                if sum([1 for xx, yy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                        if is_toilet_paper(idx_r, xx, idx_c, yy)]) < 4:
                    removable.append((idx_r, idx_c))
                    if flag:
                        solution_1 += 1
                    solution_2 += 1

    for r, c in removable:
        data[r][c] = '.'
    if not removable:
        break
    flag = False


print(solution_1)
print(solution_2)