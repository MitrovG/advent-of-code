import os

from util.input import read_matrix_str

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

grid = read_matrix_str(filepath)

empty_rows = set(x for x in range(len(grid)))
empty_columns = set(x for x in range(len(grid[0])))

galaxies = set()
for idx_r, row in enumerate(grid):
    for idx_c, val in enumerate(row):
        if val == '#':
            galaxies.add((idx_r, idx_c))
            empty_rows.discard(idx_r)
            empty_columns.discard(idx_c)

galaxies_s1 = []
galaxies_s2 = []
for galaxy in galaxies:
    r, c = galaxy
    rr = sum(x < r for x in empty_rows)
    cc = sum(x < c for x in empty_columns)
    galaxies_s1.append((r + rr, c + cc))
    galaxies_s2.append((r + rr*999_999, c + cc*999_999))

solution_1 = 0
for i, g1 in enumerate(galaxies_s1):
    for g2 in galaxies_s1[i+1:]:
        solution_1 += (abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]))
print(solution_1)

solution_2 = 0
for i, g1 in enumerate(galaxies_s2):
    for g2 in galaxies_s2[i+1:]:
        solution_2 += (abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]))
print(solution_2)
