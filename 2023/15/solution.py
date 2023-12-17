import os
import re

from util.input import read_full

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_full(filepath)
parts = data.split(',')


def get_hash(key: str) -> int:

    hash_value = 0
    for key_part in key:
        key_part_ascii = ord(key_part)
        hash_value += key_part_ascii
        hash_value *= 17
        hash_value = hash_value % 256

    return hash_value


boxes = {}
solution_1 = 0
for part in parts:
    hash_value = get_hash(part)
    solution_1 += hash_value

    key, operation, focal_lens = re.split(r'(-|=)', part)
    hashed_key = get_hash(key)
    box_lenses = boxes.get(hashed_key, [])
    new_box_lenses = []
    if operation == '-':
        for box_lens in box_lenses:
            if box_lens[0] != key:
                new_box_lenses.append(box_lens)
    else:
        flag = True
        for box_lens in box_lenses:
            if box_lens[0] != key:
                new_box_lenses.append(box_lens)
            else:
                new_box_lenses.append((key, int(focal_lens)))
                flag = False
        if flag:
            new_box_lenses.append((key, int(focal_lens)))
    boxes[hashed_key] = new_box_lenses

solution_2 = 0
for box, box_lenses in boxes.items():
    for idx, box_lens in enumerate(box_lenses):
        value = (box + 1) * (idx + 1) * box_lens[1]
        solution_2 += value

print(solution_1)
print(solution_2)