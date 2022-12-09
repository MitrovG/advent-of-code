import os
from typing import Tuple

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)


def move_head(head: Tuple[int, int], direction: str) -> Tuple[int, int]:
    h = v = 0
    if direction == 'R':
        h = 1
    elif direction == 'L':
        h = -1
    elif direction == 'U':
        v = 1
    elif direction == 'D':
        v = -1

    return head[0] + h, head[1] + v


def move_tail(tail: Tuple[int, int], head: Tuple[int, int]) -> Tuple[int, int]:

    h = v = 0
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        if head[0] - tail[0] >= 1:
            h = 1
        elif head[0] - tail[0] <= -1:
            h = -1
        if head[1] - tail[1] >= 1:
            v = 1
        elif head[1] - tail[1] <= -1:
            v = -1

    new_tail = tail[0] + h, tail[1] + v
    return new_tail


visited = set()
visited.add((0, 0))
head = (0, 0)
tail = (0, 0)

knots = [(0, 0) for x in range(10)]
visited_knots = set()
visited_knots.add((0, 0))

for row in data:
    direction, steps = row.split(' ')
    steps = int(steps)

    while steps > 0:

        head = move_head(head, direction)
        tail = move_tail(tail, head)
        visited.add(tail)

        knots[0] = move_head(knots[0], direction)
        for idx in range(len(knots) - 1):
            knot_h = knots[idx]
            knot_t = knots[idx + 1]
            knots[idx + 1] = move_tail(knot_t, knot_h)
            if idx + 1 == 9:
                visited_knots.add(knots[idx + 1])

        steps -= 1

print(len(visited))
print(len(visited_knots))
