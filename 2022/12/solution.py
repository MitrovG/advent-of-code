import os

from util.input import read_matrix_str

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix_str(filepath)

part1 = True
part2 = False

queue = []
for idx_r, row in enumerate(data):
    for idx_c, col in enumerate(row):
        if part1:
            if col == 'S':
                queue.append(((idx_r, idx_c), 0))
                data[idx_r][idx_c] = 'a'
        if part2:
            if col == 'a':
                queue.append(((idx_r, idx_c), 0))

visited = set()

while True:

    (x, y), dist = queue.pop(0)
    if data[x][y] == 'E':
        queue.append(((x, y), dist))
        break

    dist += 1
    current = ord(data[x][y])
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        xx = x + dx
        yy = y + dy
        if 0 <= xx < len(data) and 0 <= yy < len(data[0]):
            if ord(data[xx][yy]) - current <= 1 and (xx, yy) not in visited:
                visited.add((xx, yy))
                queue.append(((xx, yy), dist))

solution_1 = queue[-1][-1]
print(solution_1)
