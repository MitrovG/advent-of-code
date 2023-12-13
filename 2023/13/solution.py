import os
from typing import  List

from util.input import read_string_parts

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

parts = read_string_parts(filepath)


def mirror_row_equal(row_x: List[str], row_y: List[str], is_part_1: bool = True, flag: bool = False):

    if is_part_1:
        return row_x == row_y, flag
    else:
        cnt = len([x for (x, y) in zip(row_x, row_y) if x != y])
        if cnt == 0:
            return True, flag
        elif cnt == 1 and not flag:
            return True, True
        else:
            return False, True


def find_mirror(pattern: List[List[str]], is_part_1: bool = True):
    for i in range(len(pattern) - 1):
        flag = False
        comp_result, flag = mirror_row_equal(pattern[i], pattern[i + 1], is_part_1, flag)
        if comp_result:
            j = i - 1
            k = i + 2
            while j >= 0 and k < len(pattern):
                comp_result, flag = mirror_row_equal(pattern[j], pattern[k], is_part_1, flag)
                if not comp_result:
                    break
                j -= 1
                k += 1
            if j == -1 or k == len(pattern):
                if is_part_1:
                    return i + 1
                else:
                    if flag:
                        return i + 1

    return None


patterns = []
for part in parts:
    pattern_r = [[char for char in row] for row in part.split('\n')]
    pattern_c = list(zip(*pattern_r))
    patterns.append((pattern_r, pattern_c))


solution_1 = 0
solution_2 = 0
for pattern_r, pattern_c in patterns:

    # Part 1
    mirror_r = find_mirror(pattern_r)
    if mirror_r is not None:
        solution_1 += (mirror_r * 100)
    else:
        mirror_c = find_mirror(pattern_c)
        if mirror_c is not None:
            solution_1 += mirror_c

    # Part 2
    mirror_r = find_mirror(pattern_r, is_part_1=False)
    if mirror_r is not None:
        solution_2 += (mirror_r * 100)
    else:
        mirror_c = find_mirror(pattern_c, is_part_1=False)
        if mirror_c is not None:
            solution_2 += mirror_c

print(solution_1)
print(solution_2)
