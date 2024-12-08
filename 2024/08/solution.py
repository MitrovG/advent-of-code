import os

from util.input import read_matrix_str

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix_str(filepath)

antennas = {}
for r, row in enumerate(data):
    for c, value in enumerate(row):
        if value != '.':
            antennas.setdefault(value, []).append((r, c))


def in_range(x, y):
    return 0 <= x < len(data) and 0 <= y < len(data[0])


antinodes = set()
antinodes_2 = set()
for antenna_key, antenna_val in antennas.items():
    for i, (x_a1, y_a1) in enumerate(antenna_val[:-1]):
        for (x_a2, y_a2) in antenna_val[i+1:]:
            delta_x = x_a1 - x_a2
            delta_y = y_a1 - y_a2
            x_an1, x_an2, y_an1, y_an2 = x_a1, x_a2, y_a1, y_a2
            antinodes_2.add((x_an1, y_an1))
            antinodes_2.add((x_an2, y_an2))
            flag = True
            while True:
                x_an1 = x_an1 + delta_x
                y_an1 = y_an1 + delta_y
                if in_range(x_an1, y_an1):
                    if flag:
                        antinodes.add((x_an1, y_an1))
                        flag = False
                    antinodes_2.add((x_an1, y_an1))
                else:
                    break
            flag = True
            while True:
                x_an2 = x_an2 - delta_x
                y_an2 = y_an2 - delta_y
                if in_range(x_an2, y_an2):
                    if flag:
                        antinodes.add((x_an2, y_an2))
                        flag = False
                    antinodes_2.add((x_an2, y_an2))
                else:
                    break

solution_1 = len(antinodes)
solution_2 = len(antinodes_2)
print(sorted(antinodes_2))
print(solution_1)
print(solution_2)
