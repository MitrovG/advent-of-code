import os
import re

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)

beacons = set()
visited = set()

y = 2_000_000

initial_intervals = []
for row in data:
    sx, sy, bx, by = map(int, re.findall(r'-?\d+', row))

    beacons.add((bx, by))

    manhattan = abs(sx - bx) + abs(sy - by)
    dy = abs(sy - y)
    dx = manhattan - dy
    if dx > 0:
        initial_intervals.append((sx - dx, sx + dx))

initial_intervals.sort()
intervals = [initial_intervals[0]]
for interval in initial_intervals[1:]:

    last_interval = intervals[-1]
    if last_interval[0] <= interval[0] <= last_interval[1] + 1:
        intervals[-1] = (last_interval[0], max(last_interval[1], interval[1]))
    else:
        intervals.append(interval)

solution_1 = sum([to_ - from_ + 1 for from_, to_ in intervals])
solution_1 -= len([x for x in beacons if x[1] == y])
print(solution_1)
