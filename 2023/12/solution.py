import os
import functools
from typing import Tuple

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)


@functools.lru_cache()
def combinations(springs: str, groups: Tuple[int]):

    if not springs and not groups:
        return 1
    if not springs:
        return 0
    if not groups:
        if '#' not in springs:
            return 1
        else:
            return 0

    current_spring = springs[0]
    current_group = groups[0]

    result = 0
    if current_spring in '.?':
        result += combinations(springs[1:], groups)
    if current_spring in '#?':
        condition_1 = all(x in '?#' for x in springs[:current_group])
        condition_2a = len(springs) == current_group
        condition_2b = len(springs) > current_group and springs[current_group] in '.?'
        condition_2 = condition_2a or condition_2b
        if condition_1 and condition_2:
            result += combinations(springs[current_group + 1:], groups[1:])

    return result


solution_1 = 0
solution_2 = 0
for row in data:
    schema, groups = row.split()
    groups = tuple(map(int, groups.split(',')))
    solution_1 += combinations(schema, groups)
    schema_p2 = '?'.join([schema] * 5)
    groups_p2 = groups * 5
    solution_2 += combinations(schema_p2, groups_p2)

print(solution_1)
print(solution_2)
