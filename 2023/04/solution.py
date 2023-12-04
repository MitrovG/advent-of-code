import os
from collections import Counter

from util.input import read_string_list

directory_name = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory_name, 'input.txt')

data = read_string_list(filepath)

copy_cards = Counter()
solution_1 = 0
solution_2 = 0
for idx, row in enumerate(data):

    copy_cards[idx] += 1

    _, numbers = row.split(':')
    winning_numbers, elf_numbers = numbers.split('|')
    s_winning_numbers = {int(number.strip()) for number in winning_numbers.split()}
    s_elf_numbers = {int(number.strip()) for number in elf_numbers.split()}
    score = len(s_winning_numbers.intersection(s_elf_numbers))
    if score > 0:

        value = 2 ** (score - 1)
        solution_1 += value

        for new_idx in range(idx + 1, idx + score + 1):
            copy_cards[new_idx] += copy_cards[idx]

print(solution_1)
solution_2 = sum(copy_cards.values())
print(solution_2)