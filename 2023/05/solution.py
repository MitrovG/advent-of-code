import os
from util.input import read_string_parts

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_parts(filepath)

import re

# Initialize
seeds = list(map(int, re.findall(r'\d+', data[0])))

maps = {}
for i in range(7):
    maps[i] = [(int(s), int(s) + int(r), int(d)) for d, s, r in (row.split() for row in data[i + 1].split('\n')[1:])]

# Part 1
locations = []
for seed in seeds:
    value = seed
    for i in range(7):
        for (start, end, dest) in maps[i]:
            if start <= value < end:
                value = dest + (value - start)
                break
    locations.append(value)

solution_1 = min(locations)
print(solution_1)


# Part 2
new_seeds = []
for i in range(0,len(seeds), 2):
    new_seeds.append([seeds[i], seeds[i] + seeds[i + 1] - 1])

new_locations = []
for new_seed in new_seeds:
    values = [(new_seed[0], new_seed[1])]
    for i in range(7):
        new_values = []
        for min_seed, max_seed in values:
            min_seed_close = None, float('infinity')
            for (start, end, dest) in maps[i]:
                range_ = end - start - 1
                if start <= min_seed < end:
                    if max_seed < end:
                        new_values.append((dest + (min_seed - start), dest + (max_seed - start)))
                    else:
                        new_values.append((dest + (min_seed - start), dest + range_))
                        values.append((end, max_seed))
                    break
                else:
                    if start > min_seed and start - min_seed < min_seed_close[1]:
                        min_seed_close = start, start - min_seed
            else:
                if min_seed < max_seed:
                    if min_seed_close[0] is None or max_seed < min_seed_close[0]:
                        new_values.append((min_seed, max_seed))
                    else:
                        new_values.append((min_seed, min_seed_close[0] - 1))
                        values.append((min_seed_close[0], max_seed))
        values = new_values
    new_locations.append(min(x for x, y in new_values))

solution_2 = min(new_locations)
print(solution_2)