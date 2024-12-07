import os

from util.input import read_matrix_str

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix_str(filepath)

directions = ['^', '>', 'v', '<']
movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_direction(field_value):
    index = directions.index(field_value)
    return movements[index]


def switch(movement):
    index = movements.index(movement)
    return movements[(index + 1) % 4]


def out_of_range(position):
    if 0 <= position[0] <= len(data) and 0 <= position[1] <= len(data[0]):
        return False
    return True


obstacles = set()
guard = None
for r, row in enumerate(data):
    for c, value in enumerate(row):
        if value == '#':
            obstacles.add((r, c))
        elif value in ('>', '<', 'v', '^'):
            direction = get_direction(value)
            guard = (r, c, direction)

static_guard = guard
visited = set()
visited.add((guard[0], guard[1]))

# Part 1
solution_1 = 0
while True:
    r, c, (rr, cc) = guard
    position = (r + rr, c + cc)
    if out_of_range(position):
        visited.add((r, c))
        break
    if position in obstacles:
        rr, cc = switch((rr, cc))
    guard = (r + rr, c + cc, (rr, cc))
    visited.add((r, c))
solution_1 = len(visited)

# Part 2
solution_2 = 0
for field in visited:
    obstacles.add(field)
    guard = static_guard
    visited_2 = set()
    visited_2.add(guard)
    while True:
        r, c, (rr, cc) = guard
        position = (r + rr, c + cc)
        if out_of_range(position):
            break
        while position in obstacles:
            rr, cc = switch((rr, cc))
            position = (r + rr, c + cc)
        guard = (r + rr, c + cc, (rr, cc))
        if guard in visited_2:
            solution_2 += 1
            break
        visited_2.add(guard)
    obstacles.remove(field)

print(solution_1)
print(solution_2)
