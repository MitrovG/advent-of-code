import os

from util.input import read_matrix_str

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix_str(filepath)


def in_range(x, y):
    return 0 <= x < len(data) and 0 <= y < len(data[0])


# Part 1
q = [(x, y) for x, row in enumerate(data) for y, value in enumerate(row) if value == 'X']
queue = []
for i, j in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
    for r, c in q:
        queue.append((r, c, i, j))

for letter in ['M', 'A', 'S']:
    new_queue = []
    while queue:
        r, c, i, j = queue.pop()
        xx = r + i
        yy = c + j
        if in_range(xx, yy) and data[xx][yy] == letter:
            new_queue.append((xx, yy, i, j))
    queue = new_queue

solution_1 = len(queue)

# Part 2
q2 = [(x, y) for x, row in enumerate(data) for y, value in enumerate(row) if value == 'A']

solution_2 = 0
for r, c in q2:
    rd = r + 1
    ru = r - 1
    cr = c + 1
    cl = c - 1
    if in_range(rd, cr) and in_range(rd, cl) and in_range(ru, cr) and in_range(ru, cl):
        if sorted([data[rd][cr], 'A', data[ru][cl]]) == sorted('MAS') == sorted([data[rd][cl], 'A', data[ru][cr]]):
            solution_2 += 1

print(solution_1)
print(solution_2)
