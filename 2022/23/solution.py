from __future__ import annotations
import os
from collections import Counter
from typing import Tuple, List

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)


def should_move(elf: Tuple[int, int]) -> bool:
    xx, yy = elf
    positions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    if any((xx + dx, yy + dy) in elves for (dx, dy) in positions):
        return True

    return False


def move_elf(elf: Tuple[int, int], directions: List[List[Tuple[int, int]]]) -> Tuple[int, int]:
    xx, yy = elf
    for direction in directions:
        if any((xx + dx, yy + dy) in elves for (dx, dy) in direction[:-1]):
            continue
        else:
            return xx + direction[-1][0], yy + direction[-1][1]
    return xx, yy


elves = set()
directions = [[(-1, -1), (0, -1), (1, -1), (0, -1)], [(-1, 1), (0, 1), (1, 1), (0, 1)],
              [(-1, 1), (-1, 0), (-1, -1), (-1, 0)], [(1, 1), (1, 0), (1, -1), (1, 0)]]

for y, row in enumerate(data):
    for x, value in enumerate(row):
        if value == '#':
            elves.add((x, y))

idx = 1
while True:

    elf_to_elf = dict()
    new_elves = Counter()

    moved_elves = 0
    for elf in elves:
        if should_move(elf):
            new_elf = move_elf(elf, directions)
            elf_to_elf[elf] = new_elf
            new_elves[new_elf] += 1
            moved_elves += 1
        else:
            elf_to_elf[elf] = elf
            new_elves[elf] += 1

    if moved_elves == 0:
        print(f"Solution 2: {idx}")
        break

    elves.clear()
    elves.update([value if new_elves[value] < 2 else key for key, value in elf_to_elf.items()])
    directions = directions[1:] + [directions[0]]

    if idx == 10:
        left = min(x for x, y in elves)
        right = max(x for x, y in elves)
        up = min(y for x, y in elves)
        down = max(y for x, y in elves)

        area = len(range(left, right + 1)) * len(range(up, down + 1))
        solution_1 = area - len(elves)
        print(f"Solution 1: {solution_1}")
    idx += 1

