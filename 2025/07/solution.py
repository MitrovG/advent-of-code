import functools
import os

from util.input import read_matrix_str

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_matrix_str(filepath)


def in_range(rr, cc):
    return 0 <= rr < len(data) and 0 <= cc < len(data[0])


splitters = set()
tachyons = set()
solution_1 = 0
for idx_r, row in enumerate(data):
    for idx_c, value in enumerate(row):

        if value == 'S':
            tachyons.add((idx_r, idx_c))
            start = idx_r, idx_c
        elif value == '^':
            splitters.add((idx_r, idx_c))


# Part 1
while tachyons:
    new_tachyons = set()
    for r, c in tachyons:
        if not in_range(r+1, c):
            continue
        elif (r+1, c) in splitters:
            new_tachyons.add((r+1, c-1))
            new_tachyons.add((r+1, c+1))
            solution_1 += 1
        else:
            new_tachyons.add((r+1, c))
    tachyons = new_tachyons


# Part 2
@functools.lru_cache(maxsize=None)  # maxsize=None means unlimited cache size
def timelines(rr, cc):
    if not in_range(rr + 1, cc):
        return 1
    elif (rr + 1, cc) in splitters:
        return timelines(rr + 1, cc - 1) + timelines(rr + 1, cc + 1)
    else:
        return timelines(rr + 1, cc)


solution_2 = timelines(*start)

print(solution_1)
print(solution_2)