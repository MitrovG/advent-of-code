import os

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)

solution_1 = 0
solution_2 = 0
group_rucksacks = []

for idx, rucksack in enumerate(data):

    # part 1
    item_divider = len(rucksack) // 2
    first_compartment, second_compartment = set(rucksack[:item_divider]), (rucksack[item_divider:])
    similar_item: str = first_compartment.intersection(second_compartment).pop()
    if similar_item.islower():
        solution_1 += (ord(similar_item) - ord('a') + 1)
    else:
        solution_1 += (ord(similar_item) - ord('A') + 27)

    # part 2
    if idx % 3 == 0 or idx + 1 == len(data):
        if group_rucksacks:
            badge: str = set.intersection(*group_rucksacks).pop()
            if badge.islower():
                solution_2 += (ord(badge) - ord('a') + 1)
            else:
                solution_2 += (ord(badge) - ord('A') + 27)
        group_rucksacks = []
    group_rucksacks.append(set(rucksack))

print(solution_1)
print(solution_2)