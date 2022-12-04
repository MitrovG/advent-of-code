import os

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)

solution_1 = 0
solution_2 = 0
for pair_of_elves in data:
    elf_1, elf_2 = pair_of_elves.split(',')
    elf_1_min, _, elf_1_max = map(lambda x: int(x) if x != '-' else -1, elf_1.partition('-'))
    elf_2_min, _, elf_2_max = map(lambda x: int(x) if x != '-' else -1, elf_2.partition('-'))
    if (elf_1_min >= elf_2_min and elf_1_max <= elf_2_max) or \
        (elf_2_min >= elf_1_min and elf_2_max <= elf_1_max):
        solution_1 += 1
    if elf_1_min <= elf_2_max <= elf_1_max or elf_2_min <= elf_1_max <= elf_2_max:
        solution_2 += 1

print(solution_1)
print(solution_2)
