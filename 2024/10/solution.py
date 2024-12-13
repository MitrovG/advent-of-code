import os

from util.input import read_matrix

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix(filepath)


def in_range(r, c):
    return 0 <= r < len(data) and 0 <= c < len(data[0])


trailheads = [(x, y) for x, row in enumerate(data) for y, column in enumerate(row) if column == 0]

solution_1 = 0
solution_2 = 0
for trailhead in trailheads:
    peaks = set()
    queue = [(trailhead[0], trailhead[1], 0)]
    while queue:
        x, y, val = queue.pop(0)
        for xx, yy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if in_range(x+xx, y+yy) and data[x+xx][y+yy] == val + 1:
                if val == 8:
                    peaks.add((x+xx, y+yy))
                    solution_2 += 1
                else:
                    queue.append((x+xx, y+yy, val + 1))
    solution_1 += len(peaks)

print(solution_1)
print(solution_2)
