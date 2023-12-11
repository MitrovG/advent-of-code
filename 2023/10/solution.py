import os
from typing import List

from util.input import read_matrix_str

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

grid = read_matrix_str(filepath)


nodes = {}
start = None

# Setup
for idx_r, row in enumerate(grid):
    for idx_c, col in enumerate(row):

        if col == 'S':
            start = (idx_r, idx_c)
            continue
        if col == '|':
            val1 = (idx_r - 1, idx_c)
            val2 = (idx_r + 1, idx_c)
        elif col == '-':
            val1 = (idx_r, idx_c - 1)
            val2 = (idx_r, idx_c + 1)
        elif col == 'L':
            val1 = (idx_r - 1, idx_c)
            val2 = (idx_r, idx_c + 1)
        elif col == 'J':
            val1 = (idx_r - 1, idx_c)
            val2 = (idx_r, idx_c - 1)
        elif col == '7':
            val1 = (idx_r + 1, idx_c)
            val2 = (idx_r, idx_c - 1)
        elif col == 'F':
            val1 = (idx_r + 1, idx_c)
            val2 = (idx_r, idx_c + 1)
        else:
            continue

        if 0 <= val1[0] < len(grid) and 0 <= val1[1] < len(row):
            nodes.setdefault((idx_r, idx_c), []).append(val1)

        if 0 <= val2[0] < len(grid) and 0 <= val2[1] < len(row):
            nodes.setdefault((idx_r, idx_c), []).append(val2)

# Movement

seen = [start]
# First step
curr_x, curr_y = start[0], start[1]
current_node = None
for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
        if not current_node:
            node = (curr_x + i, curr_y + j)
            paths = nodes.get(node, [])
            if paths:
                if paths[0] == start or paths[1] == start:
                    current_node = node
                    seen.append(current_node)

# Next steps
while current_node != seen[0]:
    next_nodes = nodes[current_node]
    if next_nodes[0] == seen[-2]:
        current_node = next_nodes[1]
    else:
        current_node = next_nodes[0]
    seen.append(current_node)

solution_1 = len(seen) // 2
print(solution_1)


# Solution 2
sc = []
for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
        n = (start[0] + i, start[1] + j)
        paths = nodes.get(n, [])
        if paths:
            if paths[0] == start or paths[1] == start:
                sc.append((i, j))

if (sc[0] == (-1, 0) and sc[1] == (1, 0)) or (sc[0] == (1, 0) and sc[1] == (-1, 0)):
    grid[start[0]][start[1]] = '|'
elif (sc[0] == (-1, 0) and sc[1] == (0, -1)) or (sc[0] == (0, -1) and sc[1] == (-1, 0)):
    grid[start[0]][start[1]] = 'J'
elif (sc[0] == (-1, 0) and sc[1] == (0, 1)) or (sc[0] == (0, 1) and sc[1] == (-1, 0)):
    grid[start[0]][start[1]] = 'L'
elif (sc[0] == (1, 0) and sc[1] == (0, -1)) or (sc[0] == (0, -1) and sc[1] == (1, 0)):
    grid[start[0]][start[1]] = '7'
elif (sc[0] == (1, 0) and sc[1] == (0, 1)) or (sc[0] == (0, 1) and sc[1] == (1, 0)):
    grid[start[0]][start[1]] = 'F'
else:
    grid[start[0]][start[1]] = '-'

solution_2 = 0
for row in range(len(grid)):
    is_inside = False
    previous = ''
    for col in range(len(grid[0])):
        if (row, col) in seen:
            if grid[row][col] == '|':
                is_inside = not is_inside
            elif grid[row][col] in ('F', 'L'):
                previous = grid[row][col]
            elif grid[row][col] == '7':
                if previous == 'L':
                    is_inside = not is_inside
            elif grid[row][col] == 'J':
                if previous == 'F':
                    is_inside = not is_inside
        else:
            if is_inside and (row, col) not in seen:
                solution_2 += 1

print(solution_2)
