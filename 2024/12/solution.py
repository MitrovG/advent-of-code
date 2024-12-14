import os

from util.input import read_matrix_str

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix_str(filepath)

ROW_LEN = len(data)
COL_LEN = len(data[0])


regions = {}
plants = {}
region_counter = 1


def calculate_perimeter(values):
    perimeter = 0
    values_s = set(values)
    for x, y in values:
        for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (x+xx, y+yy) not in values_s:
                perimeter += 1
    return perimeter


def calculate_sides(values):
    discarded = set()
    sides = 0
    values_s = set(values)
    for x, y in values:
        for xx, direction in [(1, 'D'), (-1, 'U')]:
            if (x, y, direction) in discarded:
                continue
            if (x+xx, y) not in values_s:
                sides += 1
                for i in range(COL_LEN):
                    if (x, y+i) in values_s and (x+xx, y+i) not in values_s:
                        discarded.add((x, y+i, direction))
                    else:
                        break
                for i in range(y+1):
                    if (x, y-i) in values_s and (x+xx, y-i) not in values_s:
                        discarded.add((x, y-i, direction))
                    else:
                        break
        for yy, direction in [(1, 'R'), (-1, 'L')]:
            if (x, y, direction) in discarded:
                continue
            if (x, y+yy) not in values_s:
                sides += 1
                for i in range(ROW_LEN):
                    if (x+i, y) in values_s and (x+i, y+yy) not in values_s:
                        discarded.add((x+i, y, direction))
                    else:
                        break
                for i in range(x+1):
                    if (x-i, y) in values_s and (x-i, y+yy) not in values_s:
                        discarded.add((x-i, y, direction))
                    else:
                        break
    return sides


for x, row in enumerate(data):
    for y, val in enumerate(row):
        if (x, y) in plants:
            continue
        queue = [(x, y)]
        while queue:
            xx, yy = queue.pop(0)
            if (xx, yy) in plants:
                continue
            plants[(xx, yy)] = region_counter
            regions.setdefault(region_counter, []).append((xx, yy))
            for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= xx + ii < len(data) and 0 <= yy + jj < len(data[0]) and data[xx+ii][yy+jj] == val:
                    queue.append((xx+ii, yy+jj))
        region_counter += 1

solution_1 = 0
solution_2 = 0
for region_key, region_values in regions.items():
    region_area = len(region_values)
    region_perimeter = calculate_perimeter(region_values)
    region_sides = calculate_sides(region_values)
    solution_1 += region_area * region_perimeter
    solution_2 += region_area * region_sides

print(solution_1)
print(solution_2)
