from __future__ import annotations
import os
import re
from typing import Tuple

from util.input import read_string_parts

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_parts(filepath)


def rotate(direction: str, rotation: str) -> str:
    if rotation == 'R':
        if direction == 'UP':
            direction = 'RIGHT'
        elif direction == 'RIGHT':
            direction = 'DOWN'
        elif direction == 'DOWN':
            direction = 'LEFT'
        elif direction == 'LEFT':
            direction = 'UP'
    elif rotation == 'L':
        if direction == 'UP':
            direction = 'LEFT'
        elif direction == 'RIGHT':
            direction = 'UP'
        elif direction == 'DOWN':
            direction = 'RIGHT'
        elif direction == 'LEFT':
            direction = 'DOWN'

    return direction


def move(position: Tuple[int, int], speed: int, direction: str):
    while speed > 0:
        y, x = position
        if direction == 'RIGHT':
            if (y, x + 1) in blocks:
                pass
            elif x + 1 > borders_h[y][1]:
                if (y, borders_h[y][0]) in blocks:
                    pass
                else:
                    x = borders_h[y][0]
            else:
                x += 1
        elif direction == 'LEFT':
            if (y, x - 1) in blocks:
                pass
            elif x - 1 < borders_h[y][0]:
                if (y, borders_h[y][1]) in blocks:
                    pass
                else:
                    x = borders_h[y][1]
            else:
                x -= 1
        elif direction == 'DOWN':
            if (y + 1, x) in blocks:
                pass
            elif y + 1 > borders_v[x][1]:
                if (borders_v[x][0], x) in blocks:
                    pass
                else:
                    y = borders_v[x][0]
            else:
                y += 1
        elif direction == 'UP':
            if (y - 1, x) in blocks:
                pass
            elif y - 1 < borders_v[x][0]:
                if (borders_v[x][1], x) in blocks:
                    pass
                else:
                    y = borders_v[x][1]
            else:
                y -= 1

        position = (y, x)
        speed -= 1

    return position


blocks = set()
borders_h = [None]
borders_v = [(100_000, -1) for _ in range(1000)]
for idx_r, row in enumerate(data[0].split('\n')):
    left = None
    right = None
    for idx_c, col in enumerate(row):
        if col in ('.', '#'):
            if left is None:
                left = idx_c + 1
            right = idx_c + 1
            if col == '#':
                blocks.add((idx_r + 1, idx_c + 1))
            borders_v[idx_c + 1] = (min(borders_v[idx_c + 1][0], idx_r + 1), max(borders_v[idx_c + 1][1], idx_r + 1))
    borders_h.append((left, right))

speeds = list(map(int, re.findall(r'\d+', data[1])))
rotations = re.findall(r'[^\d+]', data[1])
rotations.insert(0, 'R')

current_direction = 'UP'
position = (1, borders_h[1][0])
for speed, rotation in zip(speeds, rotations):
    current_direction = rotate(current_direction, rotation)
    position = move(position, speed, current_direction)

direction_sum = 0
if current_direction == 'DOWN':
    direction_sum = 1
elif current_direction == 'LEFT':
    direction_sum = 2
elif current_direction == 'UP':
    direction_sum = 3
solution_1 = 1000 * position[0] + 4 * position[1] + direction_sum
print(solution_1)
