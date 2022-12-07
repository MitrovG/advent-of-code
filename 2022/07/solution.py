import os
from collections import Counter
from typing import List

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)


def path_to_key(path_l: List[str]) -> str:
    return path_l[0] + '/'.join(path_l[1:])


def update_folder_sizes(path_l: List[str], f_size: int):
    for idx in range(len(path_l)):
        key = path_to_key(path_l[:idx+1])
        folder_sizes[key] += f_size


path = ['/']
folder_sizes = Counter()

for command in data:
    if command[0] == '$':
        if 'cd' in command:
            cd_cmd, folder = command.split('cd ')
            folder = folder.strip()
            if folder == '/':
                path = ['/']
            elif folder == '..':
                path.pop()
            else:
                path.append(folder)
    else:
        if not command.startswith('dir'):
            file_size, file = command.split()
            file_size = int(file_size)
            update_folder_sizes(path, file_size)

# Part 1
solution_1 = sum([value for (key, value) in folder_sizes.items() if value <= 100000])
print(solution_1)

# Part 2
solution_2 = 0
size_to_delete = 30_000_000 - (70_000_000 - folder_sizes['/'])
folder_sizes_by_size = folder_sizes.most_common()[::-1]
for folder, size in folder_sizes_by_size:
    if size >= size_to_delete:
        solution_2 = size
        break
print(solution_2)
