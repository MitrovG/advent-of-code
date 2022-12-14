import os

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)

# Be cautious: It takes nearly 20 seconds for solution_2
solution_1 = True


def move_sand():

    sand_x = 500
    sand_y = 0
    visited = rocks.union(sand)
    while True:

        if solution_1 and sand_y >= low_border:
            return False
        if (sand_x, sand_y + 1) not in visited:
            sand_y += 1
            continue
        if (sand_x - 1, sand_y + 1) not in visited:
            sand_x -= 1
            sand_y += 1
            continue
        if (sand_x + 1, sand_y + 1) not in visited:
            sand_x += 1
            sand_y += 1
            continue
        break

    sand.add((sand_x, sand_y))
    if not solution_1 and (sand_x, sand_y) == (500, 0):
        return False
    return True


rocks = set()
sand = set()

for row in data:
    parts = row.split(' -> ')
    for part_1, part_2 in zip(parts[:-1], parts[1:]):
        x1, y1 = map(int, part_1.split(','))
        x2, y2 = map(int, part_2.split(','))
        if x1 == x2:
            rocks.update([(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)])
        if y1 == y2:
            rocks.update([(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)])

low_border = max([x for _, x in rocks])
rocks.update([(x, low_border + 2) for x in range(0, 1000)])

while True:

    if not move_sand():
        break

print(len(sand))
