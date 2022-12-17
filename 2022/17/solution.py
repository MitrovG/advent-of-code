import os
from typing import List, Tuple

from util.input import read_full

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_full(filepath)


def move_by_jet(rock: List[Tuple[int, int]], jet: int):

    new_rock = []
    for part_of_rock in rock:
        part_of_rock_x = part_of_rock[0] + jet
        new_part_of_rock = (part_of_rock[0] + jet, part_of_rock[1])
        if 0 <= part_of_rock_x <= 6 and new_part_of_rock not in blocks:
            new_rock.append(new_part_of_rock)
        else:
            return rock

    return new_rock


def move_rock(rock: List[Tuple[int, int]]):

    new_rock = []
    for part_of_rock in rock:
        new_part_of_rock = (part_of_rock[0], part_of_rock[1] - 1)
        if new_part_of_rock not in blocks:
            new_rock.append(new_part_of_rock)
        else:
            return rock, False

    return new_rock, True


# Jets and Rocks
jets = [1 if direction == '>' else -1 for direction in data]
idx_jet = 0
no_jets = len(jets)

ROCK_1 = [(2, 4), (3, 4), (4, 4), (5, 4)]
ROCK_2 = [(2, 5), (3, 4), (3, 5), (3, 6), (4, 5)]
ROCK_3 = [(2, 4), (3, 4), (4, 4), (4, 5), (4, 6)]
ROCK_4 = [(2, 4), (2, 5), (2, 6), (2, 7)]
ROCK_5 = [(2, 4), (2, 5), (3, 4), (3, 5)]
rocks = [ROCK_1, ROCK_2, ROCK_3, ROCK_4, ROCK_5]
no_rocks = len(rocks)
idx_rock = 0

# Visited
blocks = set()
blocks.update([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
max_height = 0

cache = dict()

target_1 = 2022
target_2 = 1_000_000_000_000

cycle_height = 0
first_cycle = True

while idx_rock < target_2:

    # For part 2
    first_key = idx_rock % no_rocks
    second_key = idx_jet % no_jets
    peaks = []
    for x in range(7):
        peaks.append(max([block[1] for block in blocks if block[0] == x]))
    min_h, max_h = min(peaks), max(peaks)
    third_key = frozenset([(block[0], block[1] - max_height) for block in blocks if min_h <= block[1] <= max_h])

    my_rock = rocks[idx_rock % no_rocks]
    my_rock = [(x, y + max_height) for (x, y) in my_rock]
    while True:
        my_jet = jets[idx_jet % no_jets]
        my_rock = move_by_jet(my_rock, my_jet)
        idx_jet += 1
        my_rock, did_move = move_rock(my_rock)
        if not did_move:
            blocks.update(my_rock)
            max_height = max(max_height, max([y for x, y in my_rock]))
            break

    # For part 2
    key = (first_key, second_key, third_key)
    if key in cache and first_cycle:
        prev_idx_rock, prev_max_height = cache[key]
        delta_idx_rock = idx_rock - prev_idx_rock
        delta_height = max_height - prev_max_height
        multiplier = (target_2 - idx_rock) // delta_idx_rock
        idx_rock += (multiplier * delta_idx_rock)
        cycle_height = multiplier * delta_height
        first_cycle = False
    else:
        cache[key] = (idx_rock, max_height)
    idx_rock += 1

    if idx_rock == target_1:
        print(f'Solution 1: {max_height}')

print(f'Solution 2: {max_height + cycle_height}')
