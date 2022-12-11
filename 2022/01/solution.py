import os

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)

calories = []
elf_calories = 0
for row_calorie in data:
    if not row_calorie:
        calories.append(elf_calories)
        elf_calories = 0
    else:
        elf_calories += int(row_calorie)
calories.sort(reverse=True)

solution_1 = calories[0]
solution_2 = sum(calories[:3])

print(solution_1)
print(solution_2)
